class user :
    def __init__(self, first_name, last_name, email , age,is_rewards_member = False , gold_card_points = 0) :
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.age=age
        self.is_rewards_member=is_rewards_member
        self.gold_card_points=gold_card_points
    

    def display_info(self):
        print("user details :")
        print(f"First name : {self.first_name}")
        print(f"Last name : {self.last_name}")
        print(f"Email : {self.email}")
        print(f"Age : {self.age}")
        print(f"rewards member : {'Yes' if self.is_rewards_member else 'No'}")
        print(f"Gold Card Points :{self.gold_card_points}")
        return self
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self
    print("Enrolled successfully as a rewards member with 200 gold card points.")

    def spend_points(self, amount) :
        if self.gold_card_points >= amount:
            self.gold_card_points -= amount
            print(f"{amount} points spent. Remaining points: {self.gold_card_points}")
        else:
            print("Insufficient points.")
        return self 
user1 = user("John", "Doe", "john.doe@example.com", 30)
user1.display_info().enroll().display_info().spend_points(50).display_info() 

