from agent import ask_helpdesk


print("=" * 60)
print("AI IT HELPDESK AGENT")
print("=" * 60)


question = input("\nDescribe your IT problem: ")


print("\nAgent is analyzing the problem...\n")


answer = ask_helpdesk(question)


print("\nFINAL RESPONSE")
print("-" * 60)

print(answer)