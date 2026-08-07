import heapq
from collections import Counter
import tkinter as tk
from tkinter import messagebox, scrolledtext

class Node:
    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]

def generate_codes(node, prefix="", codebook=None):
    if codebook is None:
        codebook = {}

    if node:
        if node.char is not None:
            codebook[node.char] = prefix if prefix else "0"

        generate_codes(node.left, prefix + "0", codebook)
        generate_codes(node.right, prefix + "1", codebook)

    return codebook

def huffman_encoding(data):
    if not data:
        return "", {}

    frequencies = Counter(data)
    root = build_huffman_tree(frequencies)
    codebook = generate_codes(root)
    encoded_data = ''.join(codebook[ch] for ch in data)

    return encoded_data, codebook, frequencies

def huffman_decoding(encoded_data, codebook):
    reverse_codebook = {v: k for k, v in codebook.items()}

    decoded = ""
    current = ""

    for bit in encoded_data:
        current += bit
        if current in reverse_codebook:
            decoded += reverse_codebook[current]
            current = ""

    return decoded

def process():
    text = input_text.get("1.0", tk.END).strip()

    if text == "":
        messagebox.showwarning("Warning", "Please enter text.")
        return

    encoded, codebook, frequencies = huffman_encoding(text)
    decoded = huffman_decoding(encoded, codebook)

    freq_box.delete("1.0", tk.END)
    codebook_box.delete("1.0", tk.END)
    encoded_box.delete("1.0", tk.END)
    decoded_box.delete("1.0", tk.END)

    freq_box.insert(tk.END, str(dict(frequencies)))

    for k, v in codebook.items():
        codebook_box.insert(tk.END, f"{k} : {v}\n")

    encoded_box.insert(tk.END, encoded)
    decoded_box.insert(tk.END, decoded)

    if decoded == text:
        status.config(text="Encoding & Decoding Successful", fg="green")
    else:
        status.config(text="Error", fg="red")

def clear():
    input_text.delete("1.0", tk.END)
    freq_box.delete("1.0", tk.END)
    codebook_box.delete("1.0", tk.END)
    encoded_box.delete("1.0", tk.END)
    decoded_box.delete("1.0", tk.END)
    status.config(text="")

root = tk.Tk()
root.title("Huffman Coding GUI")
root.geometry("850x700")
root.configure(bg="#f2f2f2")

tk.Label(root, text="Huffman Coding GUI", font=("Arial", 20, "bold"), bg="#f2f2f2", fg="blue").pack(pady=10)

tk.Label(root, text="Enter Text", font=("Arial", 12, "bold"), bg="#f2f2f2").pack()

input_text = scrolledtext.ScrolledText(root, width=80, height=4)
input_text.pack(pady=5)

frame = tk.Frame(root, bg="#f2f2f2")
frame.pack()

tk.Button(frame, text="Encode & Decode", command=process, bg="green", fg="white", font=("Arial", 11, "bold"), width=18).grid(row=0, column=0, padx=10)

tk.Button(frame, text="Clear", command=clear, bg="red", fg="white", font=("Arial", 11, "bold"), width=12).grid(row=0, column=1)

status = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#f2f2f2")
status.pack(pady=10)

tk.Label(root, text="Character Frequencies", font=("Arial", 12, "bold"), bg="#f2f2f2").pack()

freq_box = scrolledtext.ScrolledText(root, width=80, height=4)
freq_box.pack()

tk.Label(root, text="Huffman Codebook", font=("Arial", 12, "bold"), bg="#f2f2f2").pack()

codebook_box = scrolledtext.ScrolledText(root, width=80, height=6)
codebook_box.pack()

tk.Label(root, text="Encoded Data", font=("Arial", 12, "bold"), bg="#f2f2f2").pack()

encoded_box = scrolledtext.ScrolledText(root, width=80, height=5)
encoded_box.pack()

tk.Label(root, text="Decoded Data", font=("Arial", 12, "bold"), bg="#f2f2f2").pack()

decoded_box = scrolledtext.ScrolledText(root, width=80, height=4)
decoded_box.pack()

root.mainloop()
