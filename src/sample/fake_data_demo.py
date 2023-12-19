## https://zetcode.com/python/faker/

from faker import Faker

fake: Faker = Faker()


def simple(fake: Faker = fake):
    print(f"\n[ Simple Fakes ]\n")
    name = fake.name()
    address = fake.address()
    text = fake.text()
    print(
        f"""Simple:
Name: {name}
Address: {address}
Text: {text}          
"""
    )


def fake_names(fake: Faker = fake):
    print(f"\n[ Fake Names ]\n")
    name = fake.name()
    first_name = fake.first_name()
    last_name = fake.last_name()
    print(
        f"""Generic names:
Name: {name}
First Name: {first_name}
Last Name: {last_name}
"""
    )

    male_name = fake.name_male()
    male_first_name = fake.first_name_male()
    male_last_name = fake.last_name_male()
    print(
        f"""Male names:
Name: {male_name}
First Name: {male_first_name}
Last Name: {male_last_name}
"""
    )

    female_name = fake.name_male()
    female_first_name = fake.first_name_female()
    female_last_name = fake.last_name_female()
    print(
        f"""Female names:
Name: {female_name}
First Name: {female_first_name}
Last Name: {female_last_name}
"""
    )

    nonbinary_name = fake.name_nonbinary()
    nonbinary_first_name = fake.first_name_nonbinary()
    nonbinary_last_name = fake.last_name_nonbinary()
    print(
        f"""Nonbinary names:
Name: {nonbinary_name}
First Name: {nonbinary_first_name}
Last Name: {nonbinary_last_name}
"""
    )

    prefix = fake.prefix()
    prefix_male = fake.prefix_male()
    prefix_female = fake.prefix_female()
    prefix_nonbinary = fake.prefix_nonbinary()
    print(
        f"""Prefixes:
Prefix: {prefix}
Prefix Male: {prefix_male}
Prefix Female: {prefix_female}
Prefix Nonbinary: {prefix_nonbinary}          
"""
    )

    suffix = fake.suffix()
    suffix_male = fake.suffix_male()
    suffix_female = fake.suffix_female()
    suffix_nonbinary = fake.suffix_nonbinary()
    print(
        f"""Suffixes:
Suffix: {suffix}
Suffix Male: {suffix_male}
Suffix Female: {suffix_female}
Suffix Nonbinary: {suffix_nonbinary}          
"""
    )

    profile = fake.profile()
    print(
        f"""Profile:
{profile}
"""
    )

    job = fake.job()
    print(
        f"""Job:
{job}
"""
    )


def fake_locales():
    print(f"\n[ Localized ]\n")
    ## Czech locale
    _locale = "cz_CZ"
    fake_locale = Faker(_locale)

    name = fake_locale.name()
    address = fake_locale.address()
    phone = fake_locale.phone_number()

    print(
        f"""Locale: {fake_locale}
Name: {name}
Address: {address}
Phone: {phone}          
"""
    )


def fake_currencies():
    print(f"\n[ Currencies ]\n")
    currency = fake.currency()
    currency_name = fake.currency_name()
    currency_code = fake.currency_code()

    print(
        f"""Currency:
Currency: {currency}
Currency Name: {currency_name}
Currency Code: {currency_code}          
"""
    )


def fake_words():
    print(f"\n[ Words ]\n")
    word = fake.word()
    six_words = fake.words(6)

    words_list = ["forest", "blue", "cloud", "sky", "wood", "falcon"]
    print(
        f"""Fake Words:
Word: {word}
6 words: {six_words}
Random Fake from List: {fake.words(nb=3, ext_word_list=words_list, unique=True)}
"""
    )


def fake_profiles():
    print(f"\n[ Profiles ]\n")
    profile1 = fake.simple_profile()
    profile2 = fake.simple_profile("M")
    profile3 = fake.simple_profile("F")
    print(
        f"""Profiles:
Profile1: {profile1}
Profile2: {profile2}
Profile3: {profile3}          
"""
    )


def fake_numbers():
    print(f"\n[ Numbers ]\n")
    _int = fake.random_int()
    _int2 = fake.random_int(0, 100)
    _digit = fake.random_digit()
    print(
        f"""Numbers:
Integer: {_int}
Integer2: {_int2}
Digit: {_digit}        
"""
    )


def fake_hashes():
    print(f"\n[ Hashes ]\n")
    md5 = fake.md5()
    sha1 = fake.sha1()
    sha256 = fake.sha256()
    print(
        f"""Hashes:
MD5: {md5}
SHA1: {sha1}
SHA256: {sha256}          
"""
    )


def fake_uuids():
    print(f"\n[ UUID ]\n")
    _uuid = fake.uuid4()
    print(
        f"""UUID:
{_uuid}
"""
    )


def fake_internet_data():
    print(f"\n[ Internet Data ]\n")
    email = fake.email()
    safe_email = fake.safe_email()
    free_email = fake.free_email()
    company_email = fake.company_email()

    hostname = fake.hostname()
    domain_name = fake.domain_name()
    domain_word = fake.domain_word()
    tld = fake.tld()

    ipv4 = fake.ipv4()
    ipv6 = fake.ipv6()
    mac = fake.mac_address()

    slug = fake.slug()
    img_url = fake.image_url()

    print(
        f"""Internet:
Email: {email}
Safe Email: {safe_email}
Free Email: {free_email}
Company Email: {company_email}

Hostname: {hostname}
Domain Name: {domain_name}
Domain Word: {domain_word}
TLD: {tld}

IPv4: {ipv4}
IPv6: {ipv6}
MAC Address: {mac}

Slug: {slug}
Image URL: {img_url}          
"""
    )


def fake_datetime():
    print(f"\n[ Dates/Datetimes ]\n")
    dob = fake.date_of_birth()
    century = fake.century()
    year = fake.year()
    month = fake.month()
    month_name = fake.month_name()
    day_of_week = fake.day_of_week()
    day_of_month = fake.day_of_month()
    tz = fake.timezone()
    am_pm = fake.am_pm()

    dt_this_century = fake.date_time_this_century()
    dt_this_decade = fake.date_time_this_decade()
    dt_this_year = fake.date_time_this_year()
    dt_this_month = fake.date_time_this_month()

    date_this_century = fake.date_this_century()
    date_this_decade = fake.date_this_decade()
    date_this_year = fake.date_this_year()
    date_this_month = fake.date_this_month()

    ## 2 days
    TIME_SERIES_PRECISION = 60 * 60 * 24 * 2
    time_series = fake.time_series(
        start_date="-12d", end_date="now", precision=TIME_SERIES_PRECISION
    )

    unix_time = fake.unix_time()
    date_time = fake.date_time()
    iso8601 = fake.iso8601()
    date = fake.date()
    time = fake.time()

    print(
        f"""Datetimes:
Date of Birth: {dob}
Century: {century}
Year: {year}
Month: {month}
Month Name: {month_name}
Day of Week: {day_of_week}
Day of Month: {day_of_month}
Timezone: {tz}
AM/PM: {am_pm}

Datetime this Century: {dt_this_century}
Datetime this Decade: {dt_this_decade}
Datetime this Year: {dt_this_year}
Datetime this Month: {dt_this_month}

Date this Century: {date_this_century}
Date this Decade: {date_this_decade}
Date this Year: {date_this_year}
Date this Month: {date_this_month}

Datetime Series:
{[v[0] for v in time_series]}

Unix Time: {unix_time}
Datetime: {date_time}
ISO8601: {iso8601}
Date: {date}
Time: {time}
"""
    )


def fake_csv_data():
    print(f"\n[ CSV Data ]\n")
    fields = ["id", "first_name", "last_name", "occupation"]

    rows = []

    print("Generating 3 rows of fake CSV data...")
    for i in range(1, 3, 1):
        _id = i
        fname = fake.first_name()
        lname = fake.last_name()
        job = fake.job()

        row = {"id": _id, "first_name": fname, "last_name": lname, "job": job}
        rows.append(row)

    for r in rows:
        print(r)


def main():
    simple()
    fake_names()
    fake_locales()
    fake_currencies()
    fake_words()
    fake_profiles()
    fake_numbers()
    fake_hashes()
    fake_uuids()
    fake_internet_data()
    fake_datetime()
    fake_csv_data()


if __name__ == "__main__":
    main()
