import {useResumeStore} from "../store/resumeStore"
import { analyzeResumes } from "../services/api"

function AnalyzeButton() {
    const jobDescription = useResumeStore((state) => state.jobDescription)
    const files = useResumeStore((state) => state.files)
    const setResults = useResumeStore((state) => state.setResults)

    const handleAnalyze = async () => {
        const formData = new FormData();
        formData.append("job_description", jobDescription);
        files.forEach((file) => { formData.append("files", file) })
        const result = await analyzeResumes(formData);
        const candidates = result.map((item: any) => item.candidate)
        setResults(candidates)
    }
   
    return (
        <button 
        className="analyze-button"
        onClick={handleAnalyze}>

        Analyze Candidates
            
        </button>
    )
}
export default AnalyzeButton;