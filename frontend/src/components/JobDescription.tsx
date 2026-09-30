import { useResumeStore } from "../store/resumeStore"


function JobDescription() {
  const jobDescription = useResumeStore((state) => state.jobDescription);
  const setJobDescription = useResumeStore((state) => state.setJobDescription);

  return (
    <div className="job-description">
      <div className="section-heading">
        <span className="step-number">1</span>

        <div>
          <h2>Job Description</h2>
          <p>Enter the requirements for the role.</p>
        </div>
      </div>

      <textarea
        value={jobDescription}
        onChange={(event) => setJobDescription(event.target.value)}
        placeholder="Paste the job description here..."
        rows={12}
      />

      <div className="input-info">
        {jobDescription.length} characters
      </div>
    </div>
  );
}
export default JobDescription;