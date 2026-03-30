class Solution:

    def encode(self, strs: List[str]) -> str:
        endcoded = ""
        for s in strs:
            endcoded += str(len(s)) + "#" + s
        return endcoded

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            # Ensure we find a '#' delimiter
            while j < len(s) and s[j] != "#":
                j += 1
            
            # If no '#' found, break (invalid input)
            if j == len(s):
                break

            # Convert length substring safely
            length_str = s[i:j]
            if not length_str.isdigit():   # extra guard
                raise ValueError(f"Invalid length: {length_str}")

            length = int(length_str)
            
            # Extract the word
            start = j + 1
            end = start + length
            res.append(s[start:end])

            # Move pointer
            i = end
        return res