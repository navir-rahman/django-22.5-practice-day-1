from django.urls import path
from . import views
urlpatterns = [
   path('deposit/', views.DepositMoneyView.as_view(), name='deposit'),
   path('withdraw/', views.WithdrawMoneyView.as_view(), name='withdraw'),
   path('report/', views.TransactionReportView.as_view(), name='transaction_report'),
   path('loanRequest/', views.LoanRequestView.as_view(), name='loanRequest'),
   path('loan_list/', views.LoanListView.as_view(), name='loan_list'),
   path("loans/<int:loan_id>/", views.PayLoanView.as_view(), name="pay"),
   path('transfer/', views.TransferMoneyView.as_view(), name='transfer_money'),
]