rust/hive_network.rs
pub struct AgentSignal {
    pub source: String,
    pub value: String,
}

pub fn broadcast_signal(signal: AgentSignal) {
    println!("Signal from {}: {}", signal.source, signal.value);
}

pub fn consensus(signals: Vec<AgentSignal>) -> String {
    let mut result = String::new();

    for signal in signals {
        result.push_str(&signal.value);
    }

    result
}
