# Module 06 — OOP for Agents

## Mini-Project: Appointment Assistant

This is a mock appointment helper for a fictional tax office. It can tell a customer which times are open on Monday, Wednesday, or Friday by using a separate AppointmentLookup tool. The replies are produced by simple keyword rules — there is no real AI model or database. Requests that try to book, schedule, or cancel an appointment are handed off to a human (the front desk) because the assistant is not allowed to change the schedule. If this system used real customer data, a bug in the history or tool could accidentally expose private appointment information or return incorrect availability.