message_template=["Affiliate marketing is a performance-based marketing strategy where businesses reward affiliates for driving traffic or sales to their products or services. Affiliates promote the business through various channels such as websites, social media, or email marketing, and earn a commission for each successful referral. This model benefits both the business, which gains increased exposure and sales, and the affiliates, who can monetize their audience and efforts. To succeed in affiliate marketing, it's important to choose the right products or services to promote, understand your target audience, and create compelling content that encourages clicks and conversions. Additionally, building trust with your audience and maintaining transparency about your affiliate relationships can enhance your credibility and lead to long-term success in this field.","The platform you will be using is called 'Digitstem'. It is a comprehensive affiliate marketing platform that connects businesses with affiliates to promote their products and services. Digitstem offers a user-friendly interface, robust tracking and reporting tools, and a wide range of promotional materials to help affiliates succeed. As an affiliate marketer on Digitstem, you can browse through various campaigns, select the ones that align with your niche and audience, and start promoting them to earn commissions. The platform also provides support and resources to help you optimize your marketing efforts and maximize your earnings.","So to get started with Affiliate Marketing on Digitstem, you need to purchase the Ultimate Money Machine course which is available for 170 cedis. This course will provide you with comprehensive training on how to effectively promote products and services as an affiliate marketer. It covers various strategies, techniques, and best practices to help you succeed in the competitive world of affiliate marketing. By investing in this course, you'll gain valuable insights and knowledge that can significantly enhance your chances of earning commissions through the Digitstem platform. Once you've completed the course, you'll be well-equipped to start promoting campaigns and generating income as an affiliate marketer.If you are ready to make payment and get started with the Ultimate Money Machine course, please let me know and I will provide you with the necessary details to complete your purchase. This course is a crucial step in your affiliate marketing journey, and I'm confident that it will provide you with the tools and knowledge you need to succeed on the Digitstem platform. Don't hesitate to reach out if you have any questions or need further assistance with the payment process."]
while True:
    try:
     client_name=input("Please enter client name: ")
     break
    except ValueError:
        print("Invalid input. Please enter a valid name.")
while True:
    try:
     client_type=input("Please enter client type(curious, interested , ready to buy): ")
     break
    except ValueError:
        print("Invalid input. Please enter a valid client type.")
while True:
    try:
     client_concern=input("Enter client's concern or question:")
     break
    except ValueError:
            print("Invalid input. Please enter a valid concern or question.")
            

with open("client_messages.txt", "a") as file:
    file.write(f"Client Name: {client_name}\n")
    file.write(f"Client Type: {client_type}\n")
    file.write(f"Client Concern: {client_concern}\n")
if client_type.lower() == "curious" and  ("what" in client_concern.lower() or "how" in client_concern.lower()):
     message=message_template[0]
elif client_type.lower() == "interested" and  ("what " in client_concern.lower() or "how" in client_concern.lower()):
    message=message_template[1]
elif client_type.lower() == "ready to buy" and  ("i am " in client_concern.lower() or "what is " in client_concern.lower() or "payment" in client_concern.lower()):
    message=message_template[2]
else:
    message="Sorry, I don't have an answer to that question. Please contact our support team for further assistance."

print(message)
with open ("client_messages.txt", "a") as file:
    file.write(f"Response: {message}\n\n")




with open("client_messages.txt", "r") as file:
    print(f"\nClient Messages:")
    content=file.read()
    print(content)