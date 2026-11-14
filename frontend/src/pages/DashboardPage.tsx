import { useQuery } from '@tanstack/react-query'
import { api } from '../lib/axios'
import { Users, FileText, CheckSquare, AlertCircle } from 'lucide-react'

export default function DashboardPage() {
  const { data: stats, isLoading } = useQuery({
    queryKey: ['dashboard-stats'],
    queryFn: async () => {
      const response = await api.get('/reports/dashboard')
      return response.data
    },
  })

  if (isLoading) {
    return <div>Loading...</div>
  }

  const cards = [
    {
      title: 'Total Trainees',
      value: stats?.total_trainees || 0,
      icon: Users,
      color: 'bg-blue-500',
    },
    {
      title: 'Total Assessments',
      value: stats?.total_assessments || 0,
      icon: FileText,
      color: 'bg-green-500',
    },
    {
      title: 'Pending Verifications',
      value: stats?.pending_verifications || 0,
      icon: AlertCircle,
      color: 'bg-orange-500',
    },
  ]

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold text-gray-900">Dashboard</h1>
        <p className="text-gray-600 mt-1">
          Welcome to TVET e-ASSESS - Digital Practical Assessment Platform
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {cards.map((card) => (
          <div
            key={card.title}
            className="bg-white rounded-lg shadow-sm border border-gray-200 p-6"
          >
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm font-medium text-gray-600">{card.title}</p>
                <p className="text-3xl font-bold text-gray-900 mt-2">{card.value}</p>
              </div>
              <div className={`${card.color} p-3 rounded-lg`}>
                <card.icon className="w-8 h-8 text-white" />
              </div>
            </div>
          </div>
        ))}
      </div>

      <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-6">
        <h2 className="text-xl font-semibold text-gray-900 mb-4">Key Features</h2>
        <ul className="space-y-3">
          <li className="flex items-start">
            <CheckSquare className="w-5 h-5 text-green-500 mr-3 mt-0.5" />
            <span>Create and publish digital practical assessments</span>
          </li>
          <li className="flex items-start">
            <CheckSquare className="w-5 h-5 text-green-500 mr-3 mt-0.5" />
            <span>Electronic observation checklists with automated marking</span>
          </li>
          <li className="flex items-start">
            <CheckSquare className="w-5 h-5 text-green-500 mr-3 mt-0.5" />
            <span>Upload multimedia evidence (photos, videos, audio, documents)</span>
          </li>
          <li className="flex items-start">
            <CheckSquare className="w-5 h-5 text-green-500 mr-3 mt-0.5" />
            <span>Automatic generation of PDF assessment papers</span>
          </li>
          <li className="flex items-start">
            <CheckSquare className="w-5 h-5 text-green-500 mr-3 mt-0.5" />
            <span>Smart marksheets with separate oral and practical averages</span>
          </li>
          <li className="flex items-start">
            <CheckSquare className="w-5 h-5 text-green-500 mr-3 mt-0.5" />
            <span>Internal and external verification workflow</span>
          </li>
        </ul>
      </div>
    </div>
  )
}
