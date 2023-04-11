# TRAINING_DATA = [
#     (
#         "I had 1 serving of pizza for dinner.",
#         {"entities": [(5, 6, "num_of_units"), (15, 20, "food_name"), (25, 31, "meal")]},
#     ),
#     (
#         "2 servings of pasta for lunch today.",
#         {"entities": [(0, 1, "num_of_units"), (12, 17, "food_name"), (22, 27, "meal")]},
#     ),
#     (
#         "I had 2 slices of pizza for dinner.",
#         {"entities": [(7, 8, "num_of_units"), (15, 20, "food_name"), (24, 30, "meal")]},
#     ),
#     (
#         "3 tacos for lunch",
#         {"entities": [(0, 1, "num_of_units"), (2, 7, "food_name"), (11, 16, "meal")]},
#     ),
#     (
#         "I had 2 slices of pizza for dinner.",
#         {"entities": [(7, 8, "num_of_units"), (15, 20, "food_name"), (24, 30, "meal")]},
#     ),
#     (
#         "3 tacos for lunch",
#         {"entities": [(0, 1, "num_of_units"), (2, 7, "food_name"), (11, 16, "meal")]},
#     ),
#     (
#         "1 bowl of cereal for breakfast",
#         {"entities": [(0, 1, "num_of_units"), (10, 16, "food_name"), (20, 29, "meal")]},
#     ),
#     (
#         "I ate 5 cookies for a snack.",
#         {"entities": [(6, 7, "num_of_units"), (8, 15, "food_name"), (19, 24, "meal")]},
#     ),
#     (
#         "4 pieces of sushi for dinner",
#         {"entities": [(0, 1, "num_of_units"), (9, 14, "food_name"), (18, 24, "meal")]},
#     ),
#     (
#         "2 cups of coffee for breakfast",
#         {"entities": [(0, 1, "num_of_units"), (7, 13, "food_name"), (17, 26, "meal")]},
#     ),
#     (
#         "Enjoyed 3 pancakes for lunch",
#         {"entities": [(8, 9, "num_of_units"), (10, 18, "food_name"), (22, 27, "meal")]},
#     ),
#     (
#         "1 sandwich for dinner",
#         {"entities": [(0, 1, "num_of_units"), (2, 10, "food_name"), (14, 20, "meal")]},
#     ),
#     (
#         "4 pieces of fried chicken for dinner",
#         {"entities": [(0, 1, "num_of_units"), (9, 21, "food_name"), (25, 31, "meal")]},
#     ),
#     (
#         "Had 6 almonds as a snack",
#         {"entities": [(4, 5, "num_of_units"), (6, 13, "food_name"), (17, 22, "meal")]},
#     ),
#     (
#         "2 cups of tea for breakfast",
#         {"entities": [(0, 1, "num_of_units"), (7, 10, "food_name"), (14, 23, "meal")]},
#     ),
#     (
#         "I ate 1 burger for lunch",
#         {"entities": [(6, 7, "num_of_units"), (8, 14, "food_name"), (18, 23, "meal")]},
#     ),
#     (
#         "3 bowls of salad for dinner",
#         {"entities": [(0, 1, "num_of_units"), (8, 13, "food_name"), (17, 23, "meal")]},
#     ),
#     (
#         "Ate 4 hotdogs for lunch",
#         {"entities": [(4, 5, "num_of_units"), (6, 13, "food_name"), (17, 22, "meal")]},
#     ),
#     (
#         "1 slice of cake for dessert",
#         {"entities": [(0, 1, "num_of_units"), (9, 13, "food_name"), (17, 24, "meal")]},
#     ),
#     (
#         "2 scoops of ice cream for a snack",
#         {"entities": [(0, 1, "num_of_units"), (9, 18, "food_name"), (22, 27, "meal")]},
#     ),
#     (
#         "I had 5 chicken wings for dinner",
#         {"entities": [(6, 7, "num_of_units"), (8, 21, "food_name"), (25, 31, "meal")]},
#     ),
#     (
#         "3 bowls of pasta for lunch",
#         {"entities": [(0, 1, "num_of_units"), (8, 13, "food_name"), (17, 22, "meal")]},
#     ),
#     (
#         "Ate 1 donut for breakfast",
#         {"entities": [(4, 5, "num_of_units"), (6, 11, "food_name"), (15, 24, "meal")]},
#     ),
#     (
#         "Had 2 chocolate bars as a snack",
#         {"entities": [(4, 5, "num_of_units"), (6, 19, "food_name"), (23, 28, "meal")]},
#     ),
#     (
#         "I ate 3 eggs for breakfast",
#         {"entities": [(6, 7, "num_of_units"), (8, 12, "food_name"), (16, 25, "meal")]},
#     ),
#     (
#         "4 cups of orange juice for lunch",
#         {"entities": [(0, 1, "num_of_units"), (7, 18, "food_name"), (22, 27, "meal")]},
#     ),
#     (
#         "2 servings of lasagna for dinner",
#         {"entities": [(0, 1, "num_of_units"), (12, 19, "food_name"), (23, 29, "meal")]},
#     ),
#     (
#         "Enjoyed 1 muffin for a snack",
#         {"entities": [(8, 9, "num_of_units"), (10, 16, "food_name"), (20, 25, "meal")]},
#     ),
#     (
#         "I had 5 shrimp for lunch",
#         {"entities": [(6, 7, "num_of_units"), (8, 14, "food_name"), (18, 23, "meal")]},
#     ),
#     (
#         "1 piece of steak for dinner",
#         {"entities": [(0, 1, "num_of_units"), (9, 14, "food_name"), (18, 24, "meal")]},
#     ),
#     (
#         "4 fish sticks for lunch",
#         {"entities": [(0, 1, "num_of_units"), (2, 12, "food_name"), (16, 21, "meal")]},
#     ),
#     (
#         "Ate 2 bananas for breakfast",
#         {"entities": [(4, 5, "num_of_units"), (6, 13, "food_name"), (17, 26, "meal")]},
#     ),
#     (
#         "3 scoops of yogurt for a snack",
#         {"entities": [(0, 1, "num_of_units"), (9, 15, "food_name"), (19, 24, "meal")]},
#     ),
#     (
#         "1 plate of nachos for dinner",
#         {"entities": [(0, 1, "num_of_units"), (10, 16, "food_name"), (20, 26, "meal")]},
#     ),
#     (
#         "2 glasses of milk for breakfast",
#         {"entities": [(0, 1, "num_of_units"), (10, 14, "food_name"), (18, 27, "meal")]},
#     ),
#     (
#         "4 chicken nuggets for lunch",
#         {"entities": [(0, 1, "num_of_units"), (2, 16, "food_name"), (20, 25, "meal")]},
#     ),
#     (
#         "I ate a banana, 2 grapes, and 3 strawberries",
#         {
#             "entities": [
#                 (8, 14, "food_name"),
#                 (16, 17, "num_of_units"),
#                 (18, 24, "food_name"),
#                 (30, 31, "num_of_units"),
#                 (32, 44, "food_name"),
#             ]
#         },
#     ),
#     (
#         "1 sandwich, 4 cookies, and a cup of tea",
#         {
#             "entities": [
#                 (0, 1, "num_of_units"),
#                 (2, 10, "food_name"),
#                 (12, 13, "num_of_units"),
#                 (14, 21, "food_name"),
#                 (31, 34, "food_name"),
#             ]
#         },
#     ),
#     (
#         "2 slices of pizza and 3 tacos",
#         {
#             "entities": [
#                 (0, 1, "num_of_units"),
#                 (9, 14, "food_name"),
#                 (19, 20, "num_of_units"),
#                 (21, 26, "food_name"),
#             ]
#         },
#     ),
#     (
#         "Ate 1 burger, 5 fries, and 1 soda",
#         {
#             "entities": [
#                 (4, 5, "num_of_units"),
#                 (6, 12, "food_name"),
#                 (14, 15, "num_of_units"),
#                 (16, 21, "food_name"),
#                 (27, 28, "num_of_units"),
#                 (29, 33, "food_name"),
#             ]
#         },
#     ),
#     (
#         "4 sushi rolls, 2 bowls of miso soup",
#         {
#             "entities": [
#                 (0, 1, "num_of_units"),
#                 (2, 12, "food_name"),
#                 (14, 15, "num_of_units"),
#                 (23, 32, "food_name"),
#             ]
#         },
#     ),
#     (
#         "1 apple, 2 oranges, and 3 pears",
#         {
#             "entities": [
#                 (0, 1, "num_of_units"),
#                 (2, 7, "food_name"),
#                 (9, 10, "num_of_units"),
#                 (11, 18, "food_name"),
#                 (24, 25, "num_of_units"),
#                 (26, 31, "food_name"),
#             ]
#         },
#     ),
#     (
#         "2 cups of coffee, 1 croissant, and a yogurt",
#         {
#             "entities": [
#                 (0, 1, "num_of_units"),
#                 (7, 13, "food_name"),
#                 (15, 16, "num_of_units"),
#                 (17, 26, "food_name"),
#                 (36, 42, "food_name"),
#             ]
#         },
#     ),
#     (
#         "3 pancakes, 1 sausage, and 2 eggs",
#         {
#             "entities": [
#                 (0, 1, "num_of_units"),
#                 (2, 10, "food_name"),
#                 (12, 13, "num_of_units"),
#                 (14, 21, "food_name"),
#                 (27, 28, "num_of_units"),
#                 (29, 33, "food_name"),
#             ]
#         },
#     ),
#     (
#         "Ate a salad, 1 slice of cake, and 2 scoops of ice cream",
#         {
#             "entities": [
#                 (6, 11, "food_name"),
#                 (13, 14, "num_of_units"),
#                 (21, 25, "food_name"),
#                 (31, 32, "num_of_units"),
#                 (39, 48, "food_name"),
#             ]
#         },
#     ),
#     (
#         "2 hotdogs, 3 chicken wings, and a bag of chips",
#         {
#             "entities": [
#                 (0, 1, "num_of_units"),
#                 (2, 9, "food_name"),
#                 (11, 12, "num_of_units"),
#                 (13, 26, "food_name"),
#                 (36, 44, "food_name"),
#             ]
#         },
#     ),
#     (
#         "1 bowl of cereal, 2 toasts, and a glass of orange juice",
#         {
#             "entities": [
#                 (0, 1, "num_of_units"),
#                 (10, 16, "food_name"),
#                 (18, 19, "num_of_units"),
#                 (20, 26, "food_name"),
#                 (36, 49, "food_name"),
#             ]
#         },
#     ),
#     (
#         "3 carrots, 1 bell pepper, and 2 tomatoes",
#         {
#             "entities": [
#                 (0, 1, "num_of_units"),
#                 (2, 9, "food_name"),
#                 (11, 12, "num_of_units"),
#                 (13, 24, "food_name"),
#                 (30, 31, "num_of_units"),
#                 (32, 40, "food_name"),
#             ]
#         },
#     ),
#     (
#         "Ate 2 cheeseburgers and 3 servings of fries",
#         {
#             "entities": [
#                 (4, 5, "num_of_units"),
#                 (6, 18, "food_name"),
#                 (23, 24, "num_of_units"),
#                 (25, 39, "food_name"),
#             ]
#         },
#     ),
#     (
#         "4 cups of tea, 1 muffin, and 3 cookies",
#         {
#             "entities": [
#                 (0, 1, "num_of_units"),
#                 (7, 10, "food_name"),
#                 (12, 13, "num_of_units"),
#                 (14, 20, "food_name"),
#                 (26, 27, "num_of_units"),
#                 (28, 35, "food_name"),
#             ]
#         },
#     ),
#     (
#         "I ate 2 apples, a banana, and 5 strawberries",
#         {
#             "entities": [
#                 (6, 7, "num_of_units"),
#                 (8, 14, "food_name"),
#                 (19, 25, "food_name"),
#                 (31, 32, "num_of_units"),
#                 (33, 45, "food_name"),
#             ]
#         },
#     ),
#     (
#         "3 fish sticks, 1 bowl of soup, and 2 slices of bread",
#         {
#             "entities": [
#                 (0, 1, "num_of_units"),
#                 (2, 12, "food_name"),
#                 (14, 15, "num_of_units"),
#                 (23, 27, "food_name"),
#                 (33, 34, "num_of_units"),
#                 (42, 47, "food_name"),
#             ]
#         },
#     ),
#     (
#         "1 chocolate bar, 2 almonds, and 4 cashews",
#         {
#             "entities": [
#                 (0, 1, "num_of_units"),
#                 (2, 15, "food_name"),
#                 (17, 18, "num_of_units"),
#                 (19, 26, "food_name"),
#                 (32, 33, "num_of_units"),
#                 (34, 41, "food_name"),
#             ]
#         },
#     ),
#     (
#         "Ate a bagel, 1 cup of coffee, and 2 donuts",
#         {
#             "entities": [
#                 (6, 11, "food_name"),
#                 (13, 14, "num_of_units"),
#                 (21, 27, "food_name"),
#                 (33, 34, "num_of_units"),
#                 (35, 41, "food_name"),
#             ]
#         },
#     ),
#     (
#         "2 plates of pasta and 3 slices of garlic bread",
#         {
#             "entities": [
#                 (0, 1, "num_of_units"),
#                 (10, 15, "food_name"),
#                 (20, 21, "num_of_units"),
#                 (29, 40, "food_name"),
#             ]
#         },
#     ),
#     (
#         "1 cup of milk, 3 waffles, and 4 sausages",
#         {
#             "entities": [
#                 (0, 1, "num_of_units"),
#                 (7, 11, "food_name"),
#                 (13, 14, "num_of_units"),
#                 (15, 22, "food_name"),
#                 (28, 29, "num_of_units"),
#                 (30, 38, "food_name"),
#             ]
#         },
#     ),
# ]

TRAINING_DATA = [
    (
        "I had 1 serving of pizza for dinner.",
        {"entities": [(6, 7, "num_of_units"), (19, 24, "food_name"), (29, 35, "meal")]},
    ),
    (
        "I ate 2 apples, a banana, and 5 strawberries",
        {
            "entities": [
                (5, 6, "num_of_units"),
                (8, 14, "food_name"),
                (17, 23, "food_name"),
                (29, 30, "num_of_units"),
                (31, 43, "food_name"),
            ]
        },
    ),
    (
        "3 fish sticks, 1 bowl of soup, and 2 slices of bread",
        {
            "entities": [
                (0, 1, "num_of_units"),
                (2, 12, "food_name"),
                (14, 15, "num_of_units"),
                (21, 25, "food_name"),
                (31, 32, "num_of_units"),
                (39, 44, "food_name"),
            ]
        },
    ),
    (
        "1 chocolate bar, 2 almonds, and 4 cashews",
        {
            "entities": [
                (0, 1, "num_of_units"),
                (2, 15, "food_name"),
                (17, 18, "num_of_units"),
                (19, 26, "food_name"),
                (32, 33, "num_of_units"),
                (34, 41, "food_name"),
            ]
        },
    ),
    (
        "Ate a bagel, 1 cup of coffee, and 2 donuts",
        {
            "entities": [
                (6, 11, "food_name"),
                (13, 14, "num_of_units"),
                (22, 28, "food_name"),
                (34, 35, "num_of_units"),
                (36, 42, "food_name"),
            ]
        },
    ),
    (
        "2 plates of pasta and 3 slices of garlic bread",
        {
            "entities": [
                (0, 1, "num_of_units"),
                (10, 15, "food_name"),
                (20, 21, "num_of_units"),
                (29, 40, "food_name"),
            ]
        },
    ),
    (
        "1 cup of milk, 3 waffles, and 4 sausages",
        {
            "entities": [
                (0, 1, "num_of_units"),
                (9, 13, "food_name"),
                (15, 16, "num_of_units"),
                (17, 24, "food_name"),
                (30, 31, "num_of_units"),
                (32, 40, "food_name"),
            ]
        },
    ),
]
