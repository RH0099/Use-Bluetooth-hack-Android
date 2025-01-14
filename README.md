# Use-Bluetooth-hack-Android

Termux-এ এই টুল ব্যবহার করার পুরো নিয়ম সহজভাবে ব্যাখ্যা করছি। একবারে শুরু থেকে শেষ পর্যন্ত সবকিছু ধাপে ধাপে বলব যেন আপনি বা আপনার বন্ধু সহজেই বুঝতে পারেন।  

---

### **ধাপ ১: Termux প্রস্তুত করুন**  
আপনার Termux অ্যাপ খুলুন এবং নিচের কমান্ডগুলো একে একে টাইপ করুন:  

```bash
pkg update && pkg upgrade -y
pkg install python
pkg instoll git 
pip install flask
pkg instoll scapy
pkg instoll pybluez
pkg instoll mitmproxy
```

---

### **ধাপ ২: টুল চালু করুন**  
Python ফাইলটি রান করতে নিচের কমান্ড লিখুন:  

```bash
python multitool.py
```

---

### **ধাপ ৩: মেনু অপশন ব্যবহার করুন**  
টুল চালানোর পর এই মেনু আসবে:  

```
Select an Option:
1. Bluetooth Scan
2. Network Scan
3. File Sharing
4. File Receiving
5. HTTP Traffic Monitoring (MITM)
6. Exit
Enter your choice:
```

আপনার প্রয়োজন অনুযায়ী সংখ্যা টাইপ করুন এবং Enter চাপুন।  

---

### **ধাপ ৪: প্রতিটি ফিচার কিভাবে ব্যবহার করবেন**  

#### **১. Bluetooth Scan (ব্লুটুথ স্ক্যান):**  
- মেনুতে `1` টাইপ করে Enter চাপুন।  
- আশেপাশে ব্লুটুথ ডিভাইসের নাম ও MAC অ্যাড্রেস দেখতে পাবেন।  

#### **২. Network Scan (নেটওয়ার্ক স্ক্যান):**  
- মেনুতে `2` টাইপ করে Enter চাপুন।  
- একই নেটওয়ার্কে থাকা ডিভাইসগুলোর **IP অ্যাড্রেস** এবং **MAC অ্যাড্রেস** দেখতে পাবেন।  
- উদাহরণ:
  ```
  IP: 192.168.1.5, MAC: AA:BB:CC:DD:EE:FF
  ```

#### **৩. File Sharing (ফাইল শেয়ারিং):**  
- মেনুতে `3` টাইপ করে Enter চাপুন।  
- HTTP সার্ভার চালু হবে এবং একটি লিঙ্ক দেখাবে (যেমন: `http://192.168.1.5:8080`)।  
- ওই লিঙ্কে অন্য ডিভাইসের ব্রাউজার থেকে গেলে ফাইল ডাউনলোড করা যাবে।  

#### **৪. File Receiving (ফাইল রিসিভ):**  
- মেনুতে `4` টাইপ করে Enter চাপুন।  
- অন্য ডিভাইসের থেকে ফাইল আপলোড করতে পারবেন।  

#### **৫. HTTP Traffic Monitoring (MITM):**  
- মেনুতে `5` টাইপ করে Enter চাপুন।  
- আপনার নেটওয়ার্কের HTTP ট্রাফিক মনিটর করতে পারবেন।  

#### **৬. Exit (বাহির):**  
- মেনুতে `6` টাইপ করে Enter চাপলে টুল বন্ধ হয়ে যাবে।  

---

### **নোট**  
1. **রুট প্রয়োজন নেই।** তবে MITM-এর জন্য কিছু নেটওয়ার্ক কনফিগারেশনের দরকার হতে পারে।  
2. Termux-কে সব অনুমতি (Permission) দিয়ে নিন।
3. এই টুলস শুধু শিক্ষামূলক উদ্দেশ্যে ব্যবহার করবেন আনলিগ্যাল কাজে ব্যবহার করলে সেটার দায়ী আপনি থাকবেন।।
    **কোনো সমস্যায় পড়লে যোগাযোগ করুন টেলিগ্রাম আইডিতে Romgan99, আমি সাহায্য করব।**
