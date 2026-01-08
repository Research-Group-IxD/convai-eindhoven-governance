
// Card data for all phases (poster-aligned)
const phaseCards = {
	ideation: [
		{
			title: 'Ideation Brainstorm Board',
			description: 'Visual whiteboard capturing initial concept exploration and team input.',
			href: '#'
		},
		{
			title: 'Concept Plan',
			description: 'Early project scope definition and concept framing document.',
			href: '#'
		}
	],
	'proof-of-concepting': [
		{
			title: 'Mood of the Day',
			description: 'Interactive installation reflecting the city\'s current emotional state through AI.',
			href: '#'
		},
		{
			title: 'Frits is Alive',
			description: 'Conversational AI agent embodying Frits Philips\' voice and knowledge.',
			href: '#'
		},
		{
			title: 'OakAI',
			description: 'Nature-based interactive experience connecting environmental storytelling with AI.',
			href: '#'
		},
		{
			title: 'Park Whispers',
			description: 'Public space installation allowing dialogue with place-based AI personas.',
			href: '#'
		},
		{
			title: 'Gnome Hunt',
			description: 'Gamified city exploration using AR and AI-guided storytelling.',
			href: '#'
		}
	],
	'working-concept': [
		{
			title: 'Experience Flow',
			description: 'Core interaction flow and integrated concept behaviors.',
			href: '#'
		},
		{
			title: 'Prototype Demo',
			description: 'Demonstration of the working concept with key interactions.',
			href: '#'
		}
	],
	'additional-researching': [
		{
			title: 'Societal Impact Document',
			description: 'Analysis of ethical considerations and societal implications of AI heritage agents.',
			href: 'static/pdfs/Societal Impact Document-1.pdf'
		},
		{
			title: 'Competitive Analysis',
			description: 'Examination of comparable interactive installations and their strengths/gaps.',
			href: '#'
		},
		{
			title: 'Literature Study',
			description: 'Background research on Frits Philips, AI in cultural heritage, and conversational design.',
			href: '#'
		},
		{
			title: 'Target Audience & Personas',
			description: 'User profiles and needs analysis for residents and tourists engaging with the installation.',
			href: '#'
		}
	],
	'refinement-testing': [
		{
			title: 'User Test Report',
			description: 'Qualitative findings from live testing sessions with public participants.',
			href: '#'
		},
		{
			title: 'Event Poster Feedback',
			description: 'Visual communication testing and public response to event materials.',
			href: '#'
		},
		{
			title: 'Survey Results',
			description: 'Quantitative and qualitative insights from post-interaction surveys.',
			href: '#'
		},
		{
			title: 'Standups',
			description: 'Team coordination notes and sprint check-ins throughout the semester.',
			href: '#'
		},
		{
			title: 'Stakeholder Meetings',
			description: 'Insights and guidance from external partners and advisors.',
			href: '#'
		},
		{
			title: 'Retro Verslag',
			description: 'Team retrospective reflecting on process, learnings, and improvements.',
			href: '#'
		},
		{
			title: 'Legal Meeting',
			description: 'Compliance review covering data privacy, image rights, and ethical AI use.',
			href: '#'
		}
	],
	'finalizing-project': [
		{
			title: 'Final Planning',
			description: 'Master schedule with task assignments and milestone dates.',
			href: '#'
		},
		{
			title: 'Next Steps',
			description: 'Prioritized actions and immediate follow-ups post-validation phase.',
			href: '#'
		},
		{
			title: 'Project Proposal',
			description: 'Initial project scope, intent, and framework submitted at project start.',
			href: '#'
		},
		{
			title: 'Git Repo Organization',
			description: 'Branch model, role definitions, and repository structure overview.',
			href: '#'
		},
		{
			title: 'Git Workflow Guide',
			description: 'Branching strategy, PR process, and collaboration guidelines for the team.',
			href: 'GIT_WORKFLOW_GUIDE.md'
		},
		{
			title: 'Code Repository',
			description: 'GitHub project containing source code, documentation, and project files.',
			href: 'https://github.com/SuperZeekoe/convai-eindhoven-governance'
		}
	]
};

// Function to render cards for a phase
function renderPhaseCards(phaseId) {
	const cards = phaseCards[phaseId];
	if (!cards) return '';
	
	return cards.map(card => `
		<a href="${card.href}" target="_blank" class="link-card">
			<div class="link-card-content">
				<h4 class="link-card-title">${card.title}</h4>
				<p class="link-card-description">${card.description}</p>
			</div>
		</a>
	`).join('');
}

// Initialize cards when page loads

document.addEventListener('DOMContentLoaded', function() {
	const phases = [
		'ideation',
		'proof-of-concepting',
		'working-concept',
		'additional-researching',
		'refinement-testing',
		'finalizing-project'
	];
	phases.forEach(phase => {
		const container = document.querySelector(`#${phase} .link-cards`);
		if (container) {
			container.innerHTML = renderPhaseCards(phase);
		}
	});
});
