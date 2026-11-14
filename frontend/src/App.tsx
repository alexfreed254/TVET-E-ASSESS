import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { Toaster } from 'sonner'

// Pages
import LoginPage from './pages/LoginPage'
import DashboardPage from './pages/DashboardPage'
import AssessmentsPage from './pages/AssessmentsPage'
import MarksheetsPage from './pages/MarksheetsPage'
import TraineesPage from './pages/TraineesPage'
import VerificationPage from './pages/VerificationPage'
import ReportsPage from './pages/ReportsPage'

// Layout
import DashboardLayout from './components/layouts/DashboardLayout'

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      refetchOnWindowFocus: false,
      retry: 1,
    },
  },
})

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <BrowserRouter>
        <Routes>
          <Route path="/login" element={<LoginPage />} />
          
          <Route path="/" element={<DashboardLayout />}>
            <Route index element={<Navigate to="/dashboard" replace />} />
            <Route path="dashboard" element={<DashboardPage />} />
            <Route path="assessments" element={<AssessmentsPage />} />
            <Route path="marksheets" element={<MarksheetsPage />} />
            <Route path="trainees" element={<TraineesPage />} />
            <Route path="verification" element={<VerificationPage />} />
            <Route path="reports" element={<ReportsPage />} />
          </Route>
        </Routes>
      </BrowserRouter>
      <Toaster position="top-right" />
    </QueryClientProvider>
  )
}

export default App
