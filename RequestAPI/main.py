import requests
import hashlib
import sys

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching: {res.status_code}, check the api and try again.")
    return res
def read_response(response):
    print(response.text)
def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    # print (hashes)
    for h, count in hashes:
        # print(h, count)
        if h == hash_to_check:
            return count
    return 0
def pwned_api_check(password):
    # print(hashlib.sha1(password.encode('utf-8')).hexdigest())
    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1[:5], sha1[5:]
    print(first5_char, tail)
    response = request_api_data(first5_char)
    print(response)
    # return read_response(response)
    return get_password_leaks_count(response, tail)
# print(request_api_data('abc'))    
# pwned_api_check('123')
def main(args):
    # pass
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f"{password} was found {count} times .... You should probably change your password!")
        else:
            print(f"{password} was not found. Carry on!")
    return 'done!'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

