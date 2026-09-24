import JobDescription from './components/JobDescription';
import ResumeUpload from './components/ResumeUpload';
import AnalyzeButton from './components/AnalyzeButton';
import CandidateList from "./components/CandidateList";

function App() {
  return (
    <div className="app">
      <h1>Resume Matcher</h1>
      <JobDescription />
      <ResumeUpload />
      <AnalyzeButton />
      <CandidateList />
    </div>
  );
}

export default App;
