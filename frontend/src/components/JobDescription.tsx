import { useResumeStore } from "../store/resumeStore"


function JobDescription() {
    const jobDescription = useResumeStore( (state) => state.jobDescription)
    const setJobDescription = useResumeStore( (state) => state.setJobDescription)
    return (
        <div className = "job-description">
            <h2>Job Description</h2>
            <textarea placeholder="Place the job description here..."
            value={jobDescription}
            onChange={(event) => setJobDescription(event?.target.value)} />
        </div>
    )
}
export default JobDescription;