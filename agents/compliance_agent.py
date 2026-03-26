class ComplianceAgent:
    def check(self, draft_output):
        content = draft_output["content"]
        return {"status": "PASS", "content": content}