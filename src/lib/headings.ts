// Section headings in the form searches use: the compound's name plus the
// topic word ("side effects", "cycle length", "blood tests", "storage").
// Generic headings that used to repeat word for word on every page are
// rewritten here; a heading an intent map or a record sets on purpose is
// left alone unless it is one of these generic strings.
export function keywordHeading(name: string, text: string): string {
  const n = name;
  const map: Record<string, string> = {
    'At a glance': `${n} at a glance`,
    'What it is': `What is ${n}?`,
    'How it works': `How ${n} works`,
    'What the evidence level means': `${n} evidence level: what it means`,
    'Open questions and limitations': `${n}: open questions and limitations`,
    'Questions people ask': `${n} FAQ: questions people ask`,
    'Other compounds in its class': `${n} vs other compounds in its class`,
    'Biomarkers measured in studies': `${n} blood tests and markers measured in studies`,
    'Study durations': `${n} cycle length: how long studies gave it`,
    'How long did studies run?': `${n} cycle length: how long studies ran`,
    'Storage and handling': `${n} storage and handling`,
    'Storage and stability': `${n} storage and stability`,
    'Doses reported in studies': `${n} doses in published studies`,
    'What people report outside the literature': `${n} reported use outside the studies`,
    'What is commonly reported outside the literature': `${n} reported use outside the studies`,
    'Reported timelines': `${n} timeline: when effects appeared in studies`,
    'What is measured over time, and what is not': `${n} timeline: what is measured over time, and what is not`,
    'Reported interactions': `${n} interactions reported in studies`,
    'Weight-normalized doses, as published': `${n} dose per kilogram, as published`,
    'What the evidence shows': `${n} research: every study in this record`,
    'What happened in the human studies?': `${n} in human studies: what happened`,
    'What did the studies find?': `${n} research: what the studies found`,
    'Regulatory status': `Is ${n} approved? Regulatory status`,
    'Routes studied': `How ${n} is given: routes used in studies`,
    'Escalation schedules used in studies': `${n} titration: how trials stepped the dose`,
    'Studied in combination': `${n} stacks and combinations studied`,
    'Exclusion criteria in studies': `Who should avoid ${n}: who trials excluded`,
    'Adverse events and frequency': `${n} side effects and how often they occurred`,
    'What side effects have been reported?': `${n} side effects: what has been reported`,
    'What happens after a dose, and what people report over weeks': `${n} timeline: what happens after a dose, and over weeks`,
    'Routes: what the studies used': `How ${n} is given: routes the studies used`,
    'Routes used in the studies': `How ${n} is given: routes the studies used`,
    'Blood tests and monitoring that appear in the literature': `${n} blood tests and monitoring in the literature`,
    // Stacks and comparisons: n is "BPC-157 + TB-500" or "BPC-157 vs TB-500".
    'Each component on its own evidence': `${n}: each component's own evidence`,
    'Papers that name every component': `${n}: papers that name every component`,
    'Open questions': `${n}: open questions`,
    'What this stack is': `What is the ${n} stack?`,
    'Who this is discussed for, and what is unresolved': `Who ${n} is discussed for, and what is unresolved`,
    'What has been tested as a combination': `${n}: what has been tested as a combination`,
    'Common mistakes in how this stack is discussed': `Common mistakes in how ${n} is discussed`,
    'The short answer': `${n}: the short answer`,
    'Side by side, from each record': `${n} side by side`,
    'Studies that name both compounds': `${n}: studies that name both compounds`,
    'The comparison in two minutes': `${n} in two minutes`,
    'Common mistakes in this comparison': `Common mistakes when comparing ${n}`,
    'What the evidence lets you say': `${n}: what the evidence lets you say`,
    'What differs, point by point': `${n}: what differs, point by point`,
  };
  return map[text.trim()] ?? text;
}
