class AgentDashboard {
  constructor() {
    this.agents = [];
  }

  registerAgent(name) {
    this.agents.push(name);
  }

  listAgents() {
    return this.agents;
  }
}

const dashboard = new AgentDashboard();

dashboard.registerAgent("research_agent");
dashboard.registerAgent("logic_agent");

console.log(dashboard.listAgents());
