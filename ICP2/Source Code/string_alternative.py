def string_alternative(str):
    count = 0
    output_string = ""
    for c in str:
        if not c is " " or c is ",":
            count += 1
            # print(count)
            if count % 2 != 0:
                output_string += c
        else:
            output_string += c
    return output_string


def main():
    _input = input("Enter the string:-")
    output = string_alternative(_input)
    print("The output string is:-", output)


if __name__== "__main__":
  main()