from fastapi import FastAPI
from pydantic import BaseModel

from agents.draft_agent import DraftAgent
from agents.compliance_agent import ComplianceAgent
from agents.localization_agent import LocalizationAgent
from agents.distribution_agent import DistributionAgent
from agents.intelligence_agent import IntelligenceAgent

app = FastAPI()

draft = DraftAgent()
compliance = ComplianceAgent()
localization = LocalizationAgent()
distribution = DistributionAgent()
intelligence = IntelligenceAgent()

class InputData(BaseModel):
    topic: str

@app.get("/")
def home():
    return {"message": "API is working"}

@app.post("/run-pipeline")
def run_pipeline(data: InputData):
    result = {}

    d = draft.generate(data.topic)
    result["draft"] = d

    c = compliance.check(d)
    result["compliance"] = c

    l = localization.translate(c["content"])
    result["localization"] = l

    dist = distribution.publish(l)
    result["distribution"] = dist

    i = intelligence.analyze(c["content"])
    result["intelligence"] = i

    return result