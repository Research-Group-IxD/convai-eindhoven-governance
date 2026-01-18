// Card data for all phases (poster-aligned)
const phaseCards = {
  ideation: [
    {
      title: "Ideation Brainstorm Board",
      description:
        "Visual whiteboard capturing initial concept exploration and team input.",
      href: "static/pdfs/ideation/ideation document.pdf",
    },
    {
      title: "Concept Plan",
      description:
        "Early project scope definition and concept framing document.",
      href: "static/pdfs/ideation/Eindhoven_AI_Project_Proposal.pdf",
    },
  ],
  "proof-of-concepting": [
    {
      title: "Mood of the Day",
      description:
        "Interactive installation reflecting the city's current emotional state through AI.",
      href: "static/pdfs/poc/Concept Eindhoven AI.pdf",
    },
    {
      title: "Frits is Alive",
      description:
        "Conversational AI agent embodying Frits Philips' voice and knowledge.",
      href: "static/pdfs/poc/Frits is alive.pdf",
    },
    {
      title: "OakAI",
      description:
        "Nature-based interactive experience connecting environmental storytelling with AI.",
      href: "static/pdfs/poc/OakAI.pdf",
    },
    {
      title: "Park Whispers",
      description:
        "Public space installation allowing dialogue with place-based AI personas.",
      href: "static/pdfs/poc/ParkWhispers_concept.pdf",
    },
    {
      title: "Gnome Hunt",
      description:
        "Gamified city exploration using AR and AI-guided storytelling.",
      href: "static/pdfs/poc/GnomeHunt.pdf",
    },
  ],
  "working-concept": [
    {
      title: "Experience Flow",
      description: "Core interaction flow and integrated concept behaviors.",
      href: "static/pdfs/workingconcept/Frits ideas.pdf",
    },
    {
      title: "Prototype Demo",
      description:
        "Demonstration of the working concept with key interactions.",
      href: "static/pdfs/workingconcept/demo_frits.mp4",
    },
  ],
  "additional-researching": [
    {
      title: "Societal Impact Document",
      description:
        "Analysis of ethical considerations and societal implications of AI heritage agents.",
      href: "static/pdfs/Societal Impact Document-1.pdf",
    },
    {
      title: "Competitive Analysis",
      description:
        "Examination of comparable interactive installations and their strengths/gaps.",
      href: "static/pdfs/research/Competitive Analysis.pdf",
    },
    {
      title: "Literature Study Frits",
      description:
        "Background research on Frits Philips, AI in cultural heritage, and conversational design.",
      href: "static/pdfs/research/Literature Study Frits.pdf",
    },
    {
      title: "Frits deepfake Research",
      description:
        "Exploration of deepfake technology for recreating Frits Philips' likeness and voice.",
      href: "static/pdfs/research/Frits Deepfake research.pdf",
    },
    {
      title: "Location Research",
      description:
        "Study of potential installation sites within Eindhoven and their contextual relevance.",
      href: "static/pdfs/research/Location Research.pdf",
    },
    {
      title: "Research document",
      description:
        "Comprehensive summary of all research findings and references of the research phase.",
      href: "static/pdfs/research/Research Document.pdf",
    },
  ],
  "refinement-testing": [
    {
      title: "User Test Report",
      description:
        "Qualitative findings from live testing sessions with public participants.",
      href: "static/pdfs/refinement/test_report.pdf",
    },
    {
      title: "Stakeholder Meetings",
      description: "Insights and guidance from external partners and advisors.",
      href: "static/pdfs/refinement/stakeholder_meetings.pdf",
    },
    {
      title: "Legal Meeting",
      description:
        "Compliance review covering data privacy, image rights, and ethical AI use.",
      href: "static/pdfs/refinement/legal_meeting.pdf",
    },
  ],
  "finalizing-project": [
    {
      title: "Transition Report",
      description:
        "Project handover document for future researchers and developers.",
      href: "static/pdfs/Transition Report.pdf",
    },
    {
      title: "Git Repo Organization",
      description:
        "Branch model, role definitions, and repository structure overview.",
      href: "README.md",
    },
    {
      title: "Code Repository",
      description:
        "GitHub project containing source code, documentation, and project files.",
      href: "https://github.com/SuperZeekoe/convai-eindhoven-governance",
    },
  ],
};

// Function to render cards for a phase
function renderPhaseCards(phaseId) {
  const cards = phaseCards[phaseId];
  if (!cards) return "";

  return cards
    .map(
      (card) => `
		<a href="${card.href}" target="_blank" class="link-card">
			<div class="link-card-content">
				<h4 class="link-card-title">${card.title}</h4>
				<p class="link-card-description">${card.description}</p>
			</div>
		</a>
	`,
    )
    .join("");
}

// Initialize cards when page loads

document.addEventListener("DOMContentLoaded", function () {
  const phases = [
    "ideation",
    "proof-of-concepting",
    "working-concept",
    "additional-researching",
    "refinement-testing",
    "finalizing-project",
  ];
  phases.forEach((phase) => {
    const container = document.querySelector(`#${phase} .link-cards`);
    if (container) {
      container.innerHTML = renderPhaseCards(phase);
    }
  });
});
