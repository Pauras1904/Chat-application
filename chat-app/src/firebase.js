import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";
import { getStorage } from "firebase/storage";
import { getFirestore } from "firebase/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyC_fts_Ad3tDgqSwGpYPy6I-AJz0To4ybY",
  authDomain: "chatfinal-b9f4e.firebaseapp.com",
  projectId: "chatfinal-b9f4e",
  storageBucket: "chatfinal-b9f4e.appspot.com",
  messagingSenderId: "1032995090440",
  appId: "1:1032995090440:web:4cb49e6ea44efdb717a1bd",
  measurementId: "G-Z2DX531J51"
};

// Initialize Firebase
export const app = initializeApp(firebaseConfig);
export const auth = getAuth();
export const storage = getStorage();
export const db = getFirestore();