## UCLA Law Library Reservation Autofiller

This is a Python script that automatically fills out the UCLA Law Library reservation form using Selenium.

## Clone Repository

```bash
git clone https://github.com/curtischen03/LibraryReservationAutofiller.git
cd LibraryReservationAutofiller
```

## Setup

```bash
pip install selenium
pip install dotenv
```

Make sure you have **Chrome** and a compatible **ChromeDriver** installed on your system.

## Run

### Option 1:

```bash
python3 autofiller.py <firstName> <lastName> <bruinEmail> <bruinid>
```

#### Example

```bash
python3 autofiller.py Joe Bruin joebruin@g.ucla.edu 123456789
```

### Option 2:

Create .env file and fill out:

```bash
FIRST_NAME=Joe
LAST_NAME=Bruin
BRUIN_EMAIL=joebruin@g.ucla.edu
BRUIN_ID=100100100
```

Run:

```bash
python3 autofiller.py
```
### Option 3:

Currently, Github Actions is enabled, so if you put your first name, last name, bruin email, and bruin id into Github secrets, you are able to schedule every weekday at 12:00AM.


---

**Note:**
This project is for educational use only. DO NOT USE on library website. Creator is not responsible for any consequences.
