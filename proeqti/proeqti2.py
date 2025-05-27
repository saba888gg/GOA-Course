import time
import random

def print_color(text, color_code="37"):
    print(f"\033[{color_code}m{text}\033[0m")

questions = [
    {
        "type": "multiple",
        "question": "რომელი არის Python-ის სწორი ტიპი მონაცემებისთვის?",
        "options": ["A. string", "B. boolean", "C. integer", "D. ყველა ზემოთ ჩამოთვლილი"],
        "answer": "D"
    },
    {
        "type": "truefalse",
        "question": "Python-ს აქვს garbage collector? (True/False)",
        "answer": "True"
    },
    {
        "type": "text",
        "question": "რა არის Python-ში სიის შექმნის სინტაქსი?",
        "answer": "[]"
    },
    {
        "type": "multiple",
        "question": "რომელი მჭიდროდაა დაკავშირებული ხელოვნურ ინტელექტთან?",
        "options": ["A. HTML", "B. CSS", "C. Machine Learning", "D. SQL"],
        "answer": "C"
    }
]

def ask_question(q):
    print_color("\n" + q["question"], "36")
    if q["type"] == "multiple":
        for opt in q["options"]:
            print(opt)
        ans = input("👉 შეიყვანე სწორი ასო (მაგ: A): ").strip().upper()
    elif q["type"] == "truefalse":
        ans = input("👉 პასუხი (True/False): ").strip().capitalize()
    elif q["type"] == "text":
        ans = input("👉 შეიყვანე პასუხი: ").strip()
    return ans == q["answer"]

def start_quiz():
    print_color("\n🥇 კეთილი იყოს მობრძანება Python Quiz-ში!", "33")
    name = input("👉 შენი სახელი: ").strip()
    print_color(f"\n{name}, მზად ხარ კითხვებისთვის...", "35")
    time.sleep(1)

    score = 0
    random.shuffle(questions)

    for i, q in enumerate(questions, 1):
        print_color(f"\n❓ კითხვა {i}:", "34")
        if ask_question(q):
            print_color("✅ სწორია!", "32")
            score += 1
        else:
            print_color(f"❌ არასწორია. სწორი პასუხი იყო: {q['answer']}", "31")
        time.sleep(1)

    print_color(f"\n🏁 დასრულდა! შედეგი: {score}/{len(questions)}", "36")

    if score == len(questions):
        print_color("🎉 ბრწყინვალეა! Python-ის ოსტატი ხარ!", "32")
    elif score >= len(questions) // 2:
        print_color("👌 კარგია! ცოტაც და გეყოლება მაღალი ქულა!", "33")
    else:
        print_color("😅 არაუშავს, სცადე კიდევ ერთხელ!", "31")

    if input("\nგინდა თავიდან დაწყება? (კი/არა): ").strip().lower() == "კი":
        start_quiz()
    else:
        print_color("👋 მადლობა თამაშისთვის! წარმატებები!", "35")

if __name__ == "__main__":
    start_quiz()
