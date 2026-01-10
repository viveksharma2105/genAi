import tiktoken

enc =  tiktoken.encoding_for_model("gpt-4o")

text = "Hey  there! i'm Vivek Sharma"

tokens = enc.encode(text)

#Tokens [25216, 220, 1354, 0, 49232, 118495, 74, 99835]
print(f"Tokens: ",  tokens)

decode_Tokens =  enc.decode([25216, 220, 1354, 0, 49232, 118495, 74, 99835])


print(f"Decode Tokens: ", decode_Tokens)  # Decode Tokens Hey  there! i'm Vivek Sharma