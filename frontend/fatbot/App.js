import React from "react";
import { Text, View, TextInput, Button, StyleSheet } from "react-native";
import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000/"; // Change this to your backend server URL

const App = () => {
  const [userInput, setUserInput] = React.useState("");

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
    <View style={styles.container}>
      <Text>Enter your food diary entry:</Text>
      <TextInput
        onChangeText={setUserInput}
        value={userInput}
        multiline
        style={styles.textInput}
      />
      <Button title="Send" onPress={handleSendFoodEntry} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
  textInput: {
    borderColor: "gray",
    borderWidth: 1,
    width: "80%",
    marginBottom: 16,
  },
});

export default App;
