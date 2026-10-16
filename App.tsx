import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Layout from './components/Layout';
import Dashboard from './pages/Dashboard';
import EmissionAnalysis from './pages/EmissionsAnalysis';
import AIRecommendations from './pages/AIRecommendations';
import SignIn from './pages/SignIn';
import SignUp from './pages/SignUp';
import DatasetUpload from './pages/DatasetUpload';
import Simulation from './pages/Simulation';
import Reports from './pages/Reports';
import Assistant from './pages/Assistant';
import Compliance from './pages/Compliance';
import Roadmap from './pages/Roadmap';
import ROI from './pages/ROI';
import SupplyChain from './pages/SupplyChain';
import Settings from './pages/Settings';
import Landing from './pages/Landing';
import Onboarding from './pages/Onboarding';
import { useEffect, useState } from 'react';
import api from './services/api';

function App() {
  const [onboarded, setOnboarded] = useState<boolean | null>(null);
  const [loading, setLoading] = useState(true);

  const checkOnboarding = async () => {
    const token = localStorage.getItem('token');
    if (!token) {
      setLoading(false);
      return;
    }
    
    try {
      const res = await api.get('/organization');
      setOnboarded(res.data.organization?.has_onboarded || false);
    } catch (err) {
      setOnboarded(false);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    checkOnboarding();
    window.addEventListener('auth-change', checkOnboarding);
    return () => window.removeEventListener('auth-change', checkOnboarding);
  }, []);

  if (loading && localStorage.getItem('token')) {
    return <div className="min-h-screen bg-slate-900 flex items-center justify-center text-teal-500 font-black">INITIALIZING...</div>;
  }

  return (
    <Router future={{ v7_startTransition: true, v7_relativeSplatPath: true }}>
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path="/signin" element={<SignIn />} />
        <Route path="/signup" element={<SignUp />} />
        <Route path="/onboarding" element={<Onboarding />} />
        
        <Route path="/dashboard/*" element={
          onboarded === false ? <Navigate to="/onboarding" replace /> : (
          <Layout>
            <Routes>
              <Route path="/" element={<Dashboard />} />
              <Route path="/emissions" element={<EmissionAnalysis />} />
              <Route path="/recommendations" element={<AIRecommendations />} />
              <Route path="/upload" element={<DatasetUpload />} />
              <Route path="/simulation" element={<Simulation />} />
              <Route path="/reports" element={<Reports />} />
              <Route path="/assistant" element={<Assistant />} />
              <Route path="/compliance" element={<Compliance />} />
              <Route path="/roadmap" element={<Roadmap />} />
              <Route path="/roi" element={<ROI />} />
              <Route path="/supply-chain" element={<SupplyChain />} />
              <Route path="/settings" element={<Settings />} />
            </Routes>
          </Layout>
          )
        } />
      </Routes>
    </Router>
  );
}

export default App;
