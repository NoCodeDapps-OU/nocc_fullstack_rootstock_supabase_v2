from crewai import Agent
from litellm import completion

from .tools.custom_tool import (
    setup_project_tool,
    generate_contract_tool,
    generate_tests_tool,
    validate_contract_tool,
    validate_tests_tool,
    finalize_project_tool,
    frontend_html_css_tool,
    frontend_javascript_tool,
    web3js_integrate_tool,
    contract_integrate_tool,
    supabase_setup_tool,
    backend_code_generation_tool,
)

class SmartContractAgents:
    def __init__(self, model="claude-3-sonnet-20240229"):
        self.model = model
        self.llm = lambda messages: completion(model=self.model, messages=messages)

    def project_setup_agent(self):
        return Agent(
            role='Rootstock Project Manager',
            goal='Set up a new Rootstock smart contract project structure',
            backstory='You are an experienced blockchain project manager specializing in Rootstock smart contract development.',
            verbose=True,
            allow_delegation=False,
            llm=self.llm,
            tools=[setup_project_tool]
        )

    def contract_designer(self):
        return Agent(
            role='Smart Contract Designer',
            goal='Design and implement Solidity smart contracts for Rootstock based on user requirements',
            backstory='You are an expert Solidity developer with years of experience in designing secure and efficient smart contracts for Rootstock.',
            verbose=True,
            allow_delegation=False,
            llm=self.llm,
            tools=[generate_contract_tool]
        )

    def contract_tester(self):
        return Agent(
            role='Smart Contract Tester',
            goal='Create comprehensive test suites for Rootstock smart contracts',
            backstory='You are a meticulous QA engineer specializing in blockchain technology and Rootstock smart contract testing.',
            verbose=True,
            allow_delegation=False,
            llm=self.llm,
            tools=[generate_tests_tool]
        )

    def contract_validator(self):
        return Agent(
            role='Contract Validator',
            goal='Validate Rootstock smart contracts for correctness and security',
            backstory='You are an expert in Rootstock smart contract validation, responsible for ensuring contracts meet all security and functionality requirements.',
            verbose=True,
            allow_delegation=False,
            llm=self.llm,
            tools=[validate_contract_tool]
        )
    
    def test_validator(self):
        return Agent(
            role='Test Validator',
            goal='Validate and ensure the completeness of Rootstock smart contract test suites',
            backstory='You are an expert in Rootstock smart contract testing, responsible for validating test suites and ensuring they cover all aspects of the contract.',
            verbose=True,
            allow_delegation=False,
            llm=self.llm,
            tools=[validate_tests_tool]
        )

    def project_finalizer(self):
        return Agent(
            role='Project Finalizer',
            goal='Validate and finalize the Rootstock smart contract project',
            backstory='You are a senior blockchain architect responsible for ensuring the quality and completeness of Rootstock smart contract projects.',
            verbose=True,
            allow_delegation=True,
            llm=self.llm,
            tools=[
                validate_contract_tool,
                validate_tests_tool,
                finalize_project_tool
            ]
        )

class FrontendAgents:
    def __init__(self, model="claude-3-sonnet-20240229"):
        self.model = model
        self.llm = lambda messages: completion(model=self.model, messages=messages)

    def frontend_designer(self):
        return Agent(
            role='Frontend Designer',
            goal='Design and implement the frontend structure using HTML and Tailwind CSS',
            backstory='You are an expert frontend designer with years of experience in creating beautiful and responsive web interfaces.',
            verbose=True,
            allow_delegation=False,
            llm=self.llm,
            tools=[frontend_html_css_tool]
        )

    def javascript_developer(self):
        return Agent(
            role='JavaScript Developer',
            goal='Implement frontend functionality using JavaScript',
            backstory='You are a skilled JavaScript developer with expertise in creating interactive and dynamic web applications.',
            verbose=True,
            allow_delegation=False,
            llm=self.llm,
            tools=[frontend_javascript_tool]
        )

    def web3js_integrator(self):
        return Agent(
            role='Web3.js Integrator',
            goal='Integrate Web3.js components into the frontend for Rootstock interaction',
            backstory='You are an expert in blockchain technology and Web3.js integration, with a deep understanding of connecting frontends to Rootstock functionality.',
            verbose=True,
            allow_delegation=False,
            llm=self.llm,
            tools=[web3js_integrate_tool]
        )

    def contract_integrator(self):
        return Agent(
            role='Smart Contract Integrator',
            goal='Integrate the Rootstock smart contract with the frontend',
            backstory='You are a blockchain developer specializing in connecting Rootstock smart contracts to frontend applications, ensuring seamless interaction between the UI and the blockchain.',
            verbose=True,
            allow_delegation=False,
            llm=self.llm,
            tools=[contract_integrate_tool]
        )
    
class BackendAgents:
    def __init__(self, model="claude-3-sonnet-20240229"):
        self.model = model
        self.llm = lambda messages: completion(model=self.model, messages=messages)

    def supabase_integrator(self):
        return Agent(
            role='Supabase Backend Integrator',
            goal='Design and implement Supabase backend integration',
            backstory='You are an expert in backend development with extensive experience in Supabase integration.',
            verbose=True,
            allow_delegation=False,
            llm=self.llm,
            tools=[supabase_setup_tool, backend_code_generation_tool]
        )