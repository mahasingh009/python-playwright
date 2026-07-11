import csv
import json
from faker import Faker

# Initialize the Faker generator
fake = Faker()


def generate_dummy_users(count=10):
    """Generates a list of fake user profiles."""
    user_data = []

    for _ in range(count):
        # Generate a first name and last name to keep the username/email realistic
        first_name = fake.first_name()
        last_name = fake.last_name()

        # Create a clean username based on their actual fake name
        username = f"{first_name.lower()}.{last_name.lower()}{fake.random_int(min=10, max=99)}"

        user = {
            "first_name": first_name,
            "last_name": last_name,
            "username": username,
            # fake.ascii_free_email() avoids using real domain names like gmail.com
            "email": f"{username}@{fake.free_email_domain()}",
            # Generates a secure, random password
            "password": fake.password(
                length=12, special_chars=True, digits=True, upper_case=True
            ),
        }
        user_data.append(user)

    return user_data


def save_to_csv(data, filename="dummy_users.csv"):
    """Saves the generated data into a CSV file."""
    if not data:
        return

    keys = data[0].keys()
    with open(filename, "w", newline="", encoding="utf-8") as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)
    print(f"Successfully saved {len(data)} rows to {filename}")


# --- Execution ---
# if __name__ == "__main__":
#     # 1. Generate 5 sample users
#     test_users = generate_dummy_users(5)

#     # 2. Print them to the console nicely
#     print("--- Generated Dummy Data ---")
#     for user in test_users:
#         first = user['first_name']
#         last = user['last_name']
#         username = user['username']
#         email = user['email']
#         pass_word = user['password']

#         print(first)
#         print(last)
#         print(username)
#         print(email)
#         print(pass_word)

    # 3. Optional: Save to a CSV file if you need to import it elsewhere
    # print("\n--- Saving to File ---")
    # save_to_csv(test_users)


# 1. Open the file and load it into a dictionary
def read_json_file(path_file):
    with open(path_file, 'r') as file:
        data = json.load(file)
    return data

