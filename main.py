import random
import pandas
import datetime as dt
import smtplib


# Function to get today's month and day
def get_today_month_day():
    """Returns today's date in 'MM-DD' format."""
    return f"{dt.datetime.now().month}-{dt.datetime.now().day}"


class BirthdayWisher:
    """Class for sending birthday wishes."""

    def __init__(self, sender_email, password, csv_file):
        """Initialize the BirthdayWisher object."""
        self.today_month_day = get_today_month_day()  # Get today's month-day
        self.my_email = sender_email  # Email from which to send wishes
        self.my_password = password  # Email password
        self.csv_file = csv_file  # CSV file containing birthdays info
        self.birthdays_info = self.load_birthdays()  # Load the birthday info
        self.templates = []  # List to store email templates
        self.load_templates()  # Load the email templates

    def load_birthdays(self):
        """Load birthdays from a CSV file and return as a DataFrame."""
        return pandas.read_csv(self.csv_file)

    def update_bd(self, name, email, year, month, day):
        """Update the birthdays CSV with a new entry."""
        new_bd_df = pandas.DataFrame({
            "name": [name],
            "email": [email],
            "year": [year],
            "month": [month],
            "day": [day]
        })
        self.birthdays_info = pandas.concat([self.birthdays_info, new_bd_df], ignore_index=True)
        self.birthdays_info.to_csv(self.csv_file, index=False)

    def load_templates(self):
        """Load email templates from text files into a list."""
        for i in range(1, 4):
            file_name = f'letter_templates/letter_{str(i)}.txt'
            try:
                with open(file_name, mode='r') as letter:
                    self.templates.append(letter.read())
            except FileNotFoundError:
                print("File not found")

    def check_matching_bd(self):
        """Check if today is anyone's birthday and return their name and email."""
        for _, row in self.birthdays_info.iterrows():
            date = f"{row['month']}-{row['day']}"
            if date == str(self.today_month_day):
                return row['name'], row['email']
        return False

    def use_name_on_template(self, name):
        """Replace the [NAME] placeholder in a random email template with the given name."""
        temp = random.choice(self.templates)
        return temp.replace('[NAME]', name)

    def send_bd_letter(self):
        """Send the birthday email if today is someone's birthday."""
        receiver = self.check_matching_bd()
        if receiver:
            try:
                with smtplib.SMTP('smtp.gmail.com') as conn:
                    conn.starttls()
                    conn.login(user=self.my_email, password=self.my_password)
                    conn.sendmail(from_addr=self.my_email, to_addrs=receiver[1],
                                  msg=f"Subject:{self.use_name_on_template(receiver[0])}")
            except Exception as e:
                print(e)
            else:
                print("Email sent")
        else:
            print("No bd found")


bw = BirthdayWisher('your_email', 'your_password', 'your_birthdays_file.csv')
bw.send_bd_letter()
