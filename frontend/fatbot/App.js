import React from "react";
import { View, StyleSheet } from "react-native";
import axios from "axios";
import { Box, TextArea, Button, NativeBaseProvider } from "native-base";
import * as SecureStore from "expo-secure-store";
import { Linking } from "react-native";

const API_BASE_URL = "http://192.168.165.184:8000";

const App = () => {
  const [userInput, setUserInput] = React.useState("");
  const [isAuthenticated, setIsAuthenticated] = React.useState(false);

  const checkAuthentication = async () => {
    try {
      const accessToken = await SecureStore.getItemAsync("access_token");
      const accessTokenSecret = await SecureStore.getItemAsync(
        "access_token_secret"
      );
      if (accessToken && accessTokenSecret) {
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
      const response = await axios.get(`${API_BASE_URL}/oauth/start`);
      console.log("OAuth Response:", response);
      const authorizationUrl = response.data.authorization_url;
      console.log("Authorization URL:", authorizationUrl);
      // Open authorizationUrl in a browser or webview
      Linking.openURL(authorizationUrl);
    } catch (error) {
      console.error("Error starting OAuth process:", error);
    }
  };

  const handleOpenURL = async (event) => {
    const { url } = event;
    // Extract the oauth_token and oauth_verifier from the URL
    const [, queryParams] = url.split("?");
    const params = new URLSearchParams(queryParams);
    const oauth_token = params.get("oauth_token");
    const oauth_verifier = params.get("oauth_verifier");

    if (oauth_token && oauth_verifier) {
      // Send oauth_token and oauth_verifier to your backend
      try {
        const response = await axios.post(
          `${API_BASE_URL}/oauth/access_token`,
          {
            oauth_token,
            oauth_verifier,
          }
        );

        const { access_token, access_token_secret } = response.data;
        await SecureStorage.setItem("access_token", access_token);
        await SecureStorage.setItem("access_token_secret", access_token_secret);

        setIsAuthenticated(true);
      } catch (error) {
        console.error("Error getting access token:", error);
      }
    }
  };

  React.useEffect(() => {
    checkAuthentication();
    Linking.addEventListener("url", handleOpenURL);
    return () => {
      Linking.removeEventListener("url", handleOpenURL);
    };
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
      const foodEntryId = response.data.food_entry_id;
      console.log("Created food entry with ID:", foodEntryId);
    } catch (error) {
      console.error("Error sending food entry data:", error);
    }
  };

  return (
    <NativeBaseProvider>
      <View style={styles.container}>
        <Box w="100%" alignItems="center">
          <TextArea
            onChangeText={setUserInput}
            value={userInput}
            placeholder="Enter your food diary entry, include the meal, serving size, and food name.
            For example: 'I had a burger for lunch, it was 1 serving of a McDonalds burger.'"
            h={20}
            w="75%"
            //maxW="300px"
            backgroundColor={"white"}
            //borderColor="rgb(37,150,190)"
            borderWidth={1}
          />
          <Button
            title="Send Food Entry"
            onPress={handleSendFoodEntry}
            marginTop={4}
            backgroundColor={"white"}
            color="teal"
            _text={{ color: "black" }}
          >
            Send
          </Button>
        </Box>
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
