#!/usr/bin/env python3

class Solution(object):
    def decodeString(self, s):
        decoded = ''

        # True when inside an encoded strings
        reading_encoded = False
        # Index of the number for the encoded string
        encoded_start_idx = None
        # A count of open brackets
        open_brackets = 0

        #"3[a]2[bc]"
        for idx, current in enumerate(s):
            if reading_encoded:
                # Count brackets looking for the end
                if current == '[':
                    open_brackets += 1
                if current == ']':
                    open_brackets -= 1

                    if open_brackets == 0:
                        multiple = s[encoded_start_idx]

                        # Read in util we hit a [
                        i = 1
                        while s[encoded_start_idx+i].isdigit():
                            multiple += s[encoded_start_idx+i]
                            i += 1

                        contained_encoding = s[encoded_start_idx+i+1:idx]
                        contained_decoded = int(multiple) * self.decodeString(contained_encoding)
                        reading_encoded = False

                        decoded += contained_decoded

            else:
                if current.isdigit():
                    # Extract the nested encoded string
                    reading_encoded = True
                    encoded_start_idx = idx
                else:
                    decoded += current

        return decoded
