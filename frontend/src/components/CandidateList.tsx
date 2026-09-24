import { useResumeStore } from "../store/resumeStore"

function CandidateList() {
    const results = useResumeStore((state) => state.results)


return (
    <div className="candidate-list">
       <h2> Candidate Results </h2>
        {results.map((candidate, index) => (
        <div key={index}>
            <h3>{candidate.name}</h3>

            <p><b>Email:</b> {candidate.email} </p>
            <p><b>Phone:</b>  {candidate.phone}</p>
            <p><b>Location:</b> { candidate.location} </p>

            <p><b>Skills:</b> {candidate.skills.join(", ")}</p>

            <p><b>Education:</b> {candidate.education.join(", ")}</p>
            <p><b>Experience:</b>{candidate.work_experience.join(", ")}</p>

            <p><b>Certifications</b>{candidate.certifications.join(", ")}</p>

            <p><b>Match Score:</b> {candidate.match_score}%</p>

            <hr />


        </div>

       ))}
    </div>
)
}

export default CandidateList