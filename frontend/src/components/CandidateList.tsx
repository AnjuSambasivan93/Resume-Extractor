import { useResumeStore } from "../store/resumeStore"

function CandidateList() {
    const results = useResumeStore((state) => state.results)


return (
    <div className="candidate-list">
       <h2> Candidate Results </h2>
        {results.map((candidate, index) => (
        <div key={index}>
            <h3>{candidate.name}</h3>
        <p>
            Match Score: {candidate.match_score}%
        </p>
        </div>

       ))}
    </div>
)
}

export default CandidateList