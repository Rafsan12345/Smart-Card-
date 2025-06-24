import time
from smartcard.System import readers
from smartcard.Exceptions import NoCardException

# রিডার লিস্ট পাওয়া
reader_list = readers()
if not reader_list:
    print("❌ কোনো রিডার পাওয়া যায়নি!")
    exit()

reader = reader_list[0]
print("🔄 প্রস্তুত... কার্ড রিডারে রাখুন")

while True:
    try:
        # রিডার সংযোগ তৈরি
        connection = reader.createConnection()
        connection.connect()

        # UID পড়ার কমান্ড
        GET_UID = [0xFF, 0xCA, 0x00, 0x00, 0x00]
        data, sw1, sw2 = connection.transmit(GET_UID)

        if sw1 == 0x90 and sw2 == 0x00:
            uid = ''.join(['%02X' % byte for byte in data])
            print("✅ কার্ড UID:", uid)
        else:
            print("⚠️ UID পড়া যায়নি")

        # কার্ড সরাতে 1 সেকেন্ড সময় দিন
        time.sleep(1)

    except NoCardException:
        # কার্ড না থাকলে কিছু না করে অপেক্ষা
        time.sleep(0.2)

    except Exception as e:
        print("⚠️ অন্য কোনো ত্রুটি:", e)
        time.sleep(1)
