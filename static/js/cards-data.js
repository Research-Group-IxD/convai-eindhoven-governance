// Card data for all phases
const phaseCards = {
	ideation: [
		{
			icon: 'fas fa-image',
			title: 'Ideation Brainstorm Board',
			description: 'Visual whiteboard capturing initial concept exploration and team input.',
			href: '#'
		},
		{
			icon: 'fas fa-list-check',
			title: 'MoSCoW Prioritization',
			description: 'Feature prioritization framework defining must-haves, should-haves, and nice-to-haves.',
			href: '#'
		},
		{
			icon: 'fas fa-file-alt',
			title: 'Concept Plan',
			description: 'Early project scope definition and concept framing document.',
			href: '#'
		}
	],
	research: [
		{
			icon: 'fas fa-users',
			title: 'Societal Impact Document',
			description: 'Analysis of ethical considerations and societal implications of AI heritage agents.',
			href: 'static/pdfs/Societal Impact Document-1.pdf'
		},
		{
			icon: 'fas fa-chart-line',
			title: 'Competitive Analysis',
			description: 'Examination of comparable interactive installations and their strengths/gaps.',
			href: '#'
		},
		{
			icon: 'fas fa-book',
			title: 'Literature Study',
			description: 'Background research on Frits Philips, AI in cultural heritage, and conversational design.',
			href: '#'
		},
		{
			icon: 'fas fa-user-group',
			title: 'Target Audience & Personas',
			description: 'User profiles and needs analysis for residents and tourists engaging with the installation.',
			href: '#'
		}
	],
	concepting: [
		{
			icon: 'fas fa-palette',
			title: 'Mood of the Day',
			description: 'Interactive installation reflecting the city\'s current emotional state through AI.',
			href: '#'
		},
		{
			icon: 'fas fa-microphone',
			title: 'Frits is Alive',
			description: 'Conversational AI agent embodying Frits Philips\' voice and knowledge.',
			href: '#'
		},
		{
			icon: 'fas fa-tree',
			title: 'OakAI',
			description: 'Nature-based interactive experience connecting environmental storytelling with AI.',
			href: '#'
		},
		{
			icon: 'fas fa-comments',
			title: 'Park Whispers',
			description: 'Public space installation allowing dialogue with place-based AI personas.',
			href: '#'
		},
		{
			icon: 'fas fa-map-marker-alt',
			title: 'Gnome Hunt',
			description: 'Gamified city exploration using AR and AI-guided storytelling.',
			href: '#'
		}
	],
	validation: [
		{
			icon: 'fas fa-vial',
			title: 'User Test Report',
			description: 'Qualitative findings from live testing sessions with public participants.',
			href: '#'
		},
		{
			icon: 'fas fa-image',
			title: 'Event Poster Feedback',
			description: 'Visual communication testing and public response to event materials.',
			href: '#'
		},
		{
			icon: 'fas fa-chart-bar',
			title: 'Survey Results',
			description: 'Quantitative and qualitative insights from post-interaction surveys.',
			href: '#'
		},
		{
			icon: 'fas fa-calendar-check',
			title: 'Standups',
			description: 'Team coordination notes and sprint check-ins throughout the semester.',
			href: '#'
		},
		{
			icon: 'fas fa-handshake',
			title: 'Stakeholder Meetings',
			description: 'Insights and guidance from external partners and advisors.',
			href: '#'
		},
		{
			icon: 'fas fa-history',
			title: 'Retro Verslag',
			description: 'Team retrospective reflecting on process, learnings, and improvements.',
			href: '#'
		},
		{
			icon: 'fas fa-gavel',
			title: 'Legal Meeting',
			description: 'Compliance review covering data privacy, image rights, and ethical AI use.',
			href: '#'
		}
	],
	planning: [
		{
			icon: 'fas fa-calendar-alt',
			title: 'Planning',
			description: 'Master schedule with task assignments and milestone dates.',
			href: '#'
		},
		{
			icon: 'fas fa-forward',
			title: 'Next Steps',
			description: 'Prioritized actions and immediate follow-ups post-validation phase.',
			href: '#'
		},
		{
			icon: 'fas fa-clipboard-check',
			title: 'Semester Halen Lijst',
			description: 'Deliverables checklist ensuring all semester requirements are met.',
			href: '#'
		},
		{
			icon: 'fas fa-file-contract',
			title: 'Project Proposal',
			description: 'Initial project scope, intent, and framework submitted at project start.',
			href: '#'
		},
		{
			icon: 'fas fa-code-branch',
			title: 'Git Repo Organization',
			description: 'Branch model, role definitions, and repository structure overview.',
			href: '#'
		},
		{
			icon: 'fas fa-book-open',
			title: 'Git Workflow Guide',
			description: 'Branching strategy, PR process, and collaboration guidelines for the team.',
			href: 'GIT_WORKFLOW_GUIDE.md'
		},
		{
			icon: 'fab fa-github',
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
			<div class="link-card-icon">
				<i class="${card.icon}"></i>
			</div>
			<div class="link-card-content">
				<h4 class="link-card-title">${card.title}</h4>
				<p class="link-card-description">${card.description}</p>
			</div>
		</a>
	`).join('');
}

// Initialize cards when page loads
document.addEventListener('DOMContentLoaded', function() {
	const phases = ['ideation', 'research', 'concepting', 'validation', 'planning'];
	phases.forEach(phase => {
		const container = document.querySelector(`#${phase} .link-cards`);
		if (container) {
			container.innerHTML = renderPhaseCards(phase);
		}
	});
});
