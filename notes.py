begin = '\x1b[1m'
end = '\x1b[39m\x1b[22m'
red = '\x1b[31m'
blue = '\x1b[34m'
green = '\x1b[32m'
print(begin + red + 'red text' + end + ' back to normal')
print(begin + blue + 'blue text' + end + ' back to normal')
print(begin + green + 'green text' + end + ' back to normal')
