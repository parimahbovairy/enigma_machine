# enigma_machine.py

class EnigmaMachine:
    def __init__(self):
        self.letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ', "'"]
        self.letter_mapping = {'G': 7, 'U': 21, 'T': 20, 'L': 12, 'Y': 25, 'Q': 17, 'V': 22, 'J': 10, 'O': 15, 'W': 23, 'N': 14, 'R': 18, 'Z': 26, 'S': 19, 'X': 24, 'A': 1, 'M': 13, 'E': 5, 'D': 4, 'I': 9, 'F': 6, 'P': 16, 'B': 2, 'H': 8, 'K': 11, 'C': 3}
        self.rotors = {
            'rotor_one': ['J','G','D','Q','O','X','U','S','C','A','M','I','F','R','V','T','P','N','E','W','K','B','L','Z','Y','H'],
            'rotor_two': ['N','T','Z','P','S','F','B','O','K','M','W','R','C','J','D','I','V','L','A','E','Y','U','X','H','G','Q'],
            'rotor_three': ['J','V','I','U','B','H','T','C','D','Y','A','K','E','Q','Z','P','O','S','G','X','N','R','M','W','F','L']
        }
        self.reflector_disk = ['Y', 'R', 'U', 'H', 'Q', 'S', 'L', 'D', 'P', 'X', 'N', 'G', 'O', 'K', 'M', 'I', 'E', 'B', 'F', 'Z', 'C', 'W', 'V', 'J', 'A', 'T']

    def rotate_rotor(self, rotor):
        rotor.append(rotor[0])
        del rotor[0]
        return rotor

    def validate_message(self, message):
        for char in message:
            if self.letters.count(char.upper()) < 1:
                return False
        return True

    def encrypt_decrypt(self, message):
        encrypted_message = []
        for i in range(len(message)):
            if message[i] == ' ':
                encrypted_message.append(' ')
            elif message[i] == "'":
                encrypted_message.append("'")
            else:
                a = self.letter_mapping[message[i].upper()]
                b = self.rotors['rotor_one'][a-1]
                c = self.letter_mapping[b]
                d = self.rotors['rotor_two'][c-1]
                e = self.letter_mapping[d]
                f = self.rotors['rotor_three'][e-1]
                g = self.letter_mapping[f]
                h = self.reflector_disk[g-1]
                j = self.rotors['rotor_three'].index(h)
                k = self.letters[j]
                l = self.rotors['rotor_two'].index(k)
                m = self.letters[l]
                n = self.rotors['rotor_one'].index(m)
                o = self.letters[n]
                encrypted_message.append(o)

            if (i + 1) % 1 == 0:
                self.rotate_rotor(self.rotors['rotor_one'])
            if (i + 1) % 26 == 0:
                self.rotate_rotor(self.rotors['rotor_two'])
            if (i + 1) % 676 == 0:
                self.rotate_rotor(self.rotors['rotor_three'])
        return ''.join(encrypted_message)

def main():
    enigma_machine = EnigmaMachine()
    print("Hi! Welcome to the Enigma Machine ฅʕ•̫͡•ʔฅ")

    input_message = []
    while not enigma_machine.validate_message(input_message) or len(input_message) == 0:
        try:
            user_input = str(input("Write the message you want to (de)crypt: \n"))
            input_message = list(user_input)
        except:
            print("You must only enter letters without special characters!")

    result_message = enigma_machine.encrypt_decrypt(input_message)
    print("(de)crypted message: ", result_message)

if __name__ == "__main__":
    main()
