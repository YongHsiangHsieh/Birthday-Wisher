# BirthdayWisher 🎂🎉

## Description

The `BirthdayWisher` is a Python script designed to automatically send birthday emails. It loads birthday data from a CSV file and email templates from text files. If today is someone's birthday, the script sends a personalized email to the celebrant.

## Features

- Load birthdays from a CSV file
- Update the CSV file with new birthdays
- Load email templates from text files
- Send a personalized birthday email using SMTP

## Requirements

- Python 3.x
- pandas library
- smtplib library
- datetime library

## Setup

1. **Clone the repository**
    ```bash
    git clone https://github.com/YongHsiangHsieh/BirthdayWisher.git
    ```

2. **Navigate to the directory**
    ```bash
    cd BirthdayWisher
    ```

3. **Install required packages**
    ```bash
    pip install pandas
    ```

4. **Update the CSV file, `your_birthdays_file.csv`, with the birthdays**

    The CSV file should have the following columns:
    - `name`
    - `email`
    - `year`
    - `month`
    - `day`

5. **Add email templates**

    Place your email templates in text files under the `letter_templates` directory. Name them as `letter_1.txt`, `letter_2.txt`, etc.

## Usage

Update the following fields in the script:

- `your_email`: Your Gmail email address
- `your_password`: Your Gmail password (consider using [App Passwords](https://support.google.com/accounts/answer/185833?hl=en) for better security)
- `your_birthdays_file.csv`: The name of your CSV file containing the birthdays

Run the script:

```bash
python BirthdayWisher.py
```

If today is someone's birthday in the CSV file, the script will send them a personalized birthday email.

## Contributing

Feel free to fork the project and submit a pull request with your changes!
