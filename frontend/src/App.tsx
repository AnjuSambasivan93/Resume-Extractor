import JobDescription from "./components/JobDescription";
import ResumeUpload from "./components/ResumeUpload";
import AnalyzeButton from "./components/AnalyzeButton";
import CandidateList from "./components/CandidateList";

function App() {
  return (
    <div className="app">
      <header className="app-header">
        <div>
          <h1>ResumeIQ</h1>
          <p>AI-Powered Candidate Screening</p>
        </div>
      </header>

      <main className="main-content">
        <section className="hero-section">
          <h2>Find the right candidate faster</h2>
          <p>
            Add a job description and upload resumes to analyse and
            rank candidates against your requirements.
          </p>
        </section>

        <section className="screening-section">
          <div className="input-card">
            <JobDescription />
          </div>

          <div className="input-card">
            <ResumeUpload />
          </div>
        </section>

        <div className="analyze-section">
          <AnalyzeButton />
        </div>

        <section className="results-section">
          <CandidateList />
        </section>
      </main>
    </div>
  );
}

export default App;