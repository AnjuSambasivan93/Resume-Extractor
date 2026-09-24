import { create } from "zustand";
import type { Candidate } from "../types/candidate";


type ResumeStore = {
    jobDescription: string;
    files: File[];
    results: Candidate[];

    setJobDescription: (text: string) => void;
    setFiles: (files: File[]) => void;
    setResults: (results: Candidate[]) => void;
}


export const useResumeStore = create<ResumeStore>((set) => ({
    jobDescription: "",
    files: [],
    results: [],

    setJobDescription: (text: string) => set({ jobDescription: text }),
    setFiles: (files: File[]) => set({ files: files }),
    setResults: (results:any) => set({ results: results })

}))