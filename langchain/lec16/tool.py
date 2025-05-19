from langchain_community.tools import DuckDuckGoSearchRun, ShellTool

# searchtoo = DuckDuckGoSearchRun()
# result = searchtoo.invoke("AI Updates")
# print(result)

shell = ShellTool()
result = shell.invoke("ls")
print(result)