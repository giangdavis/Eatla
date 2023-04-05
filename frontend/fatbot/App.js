import React from "react";
import { View, StyleSheet } from "react-native";
import axios from "axios";
import {
  Box,
  TextArea,
  Button,
  NativeBaseProvider,
  FormControl,
  Input,
  VStack,
} from "native-base";
import * as SecureStore from "expo-secure-store";
import { Linking } from "react-native";

const API_BASE_URL = "http://192.168.165.184:8000";

// example :
// You can now use the sessionToken to make authorized requests
// Example: Fetch the profile data
// const profileResponse = await axios.get(
//   `${API_BASE_URL}/profile/${sessionToken}`
// );
// console.log("Profile Data:", profileResponse.data);

//todo: handle any errors that may occur when storing or retrieving data from SecureStore.

const App = () => {
  const [userInput, setUserInput] = React.useState("");
  const [isAuthenticated, setIsAuthenticated] = React.useState(false);
  const [pin, setPin] = React.useState("");

  const checkAuthentication = async () => {
    try {
      console.log("checking authentication");
      const accessToken = await SecureStore.getItemAsync("session_token");
      // const accessTokenSecret = await SecureStore.getItemAsync(
      //   "access_token_secret"
      // );
      if (accessToken) {
        setIsAuthenticated(true);
      } else {
        console.log("Not authenticated, starting OAuth flow...");
        startOAuth();
      }
    } catch (error) {
      console.error("Error checking authentication:", error);
      startOAuth();
    }
  };

  const startOAuth = async () => {
    try {
      console.log("in oauth start");
      const response = await axios.get(`${API_BASE_URL}/auth`);
      const authorizationUrl = response.data.auth_url;
      Linking.openURL(authorizationUrl);
    } catch (error) {
      console.error("Error starting OAuth process:", error);
    }
  };

  const handlePin = async (pin) => {
    try {
      const response = await axios.get(`${API_BASE_URL}/authenticate/${pin}`);
      const sessionToken = response.data.session_token;
      console.log("Session Token:", sessionToken);

      await SecureStore.setItemAsync("session_token", sessionToken.toString());
      setIsAuthenticated(true);
    } catch (error) {
      console.error("Error handling PIN:", error);
    }
  };

  const handlePinSubmit = () => {
    handlePin(pin);
    setPin("");
  };

  React.useEffect(() => {
    checkAuthentication();
  }, []);

  const handleSendFoodEntry = async () => {
    // Add your code here to process userInput using spaCy and obtain foodEntryData
    // For the sake of the example, we use hardcoded values
    const foodEntryData = {
      food_id: 12345,
      food_entry_name: "McDonalds Burger",
      serving_id: 67890,
      number_of_units: 1,
      meal: "lunch",
    };

    try {
      const response = await axios.post(
        `${API_BASE_URL}/create_food_entry`,
        foodEntryData
      );
      console.log("response", response.data);
    } catch (error) {
      console.error("Error sending food entry data:", error);
    }
  };

  return (
    <NativeBaseProvider>
      <View style={styles.container}>
        {!isAuthenticated && (
          <Box w="100%" alignItems="center">
            <FormControl>
              <FormControl.Label>Enter PIN:</FormControl.Label>
              <Input
                value={pin}
                onChangeText={setPin}
                placeholder="Enter the PIN provided by FatSecret"
              />
            </FormControl>
            <Button
              onPress={handlePinSubmit}
              marginTop={4}
              backgroundColor={"white"}
              color="teal"
              _text={{ color: "black" }}
            >
              Submit PIN
            </Button>
          </Box>
        )}

        {isAuthenticated && (
          <Box w="100%" alignItems="center">
            <VStack space={4} w="75%">
              <TextArea
                onChangeText={setUserInput}
                value={userInput}
                placeholder="Enter your food diary entry, include the meal, serving size, and food name.
                For example: 'I had a burger for lunch, it was 1 serving of a McDonalds burger.'"
                h={20}
                w="100%"
                backgroundColor={"white"}
                borderWidth={1}
              />
              <Button
                onPress={handleSendFoodEntry}
                backgroundColor={"white"}
                color="teal"
                _text={{ color: "black" }}
              >
                Send Food Entry
              </Button>
            </VStack>
          </Box>
        )}
      </View>
    </NativeBaseProvider>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: "#32b34c",
  },
});

export default App;
