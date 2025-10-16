# EventConnect - Project Documentation

**Project Type:** Academic Capstone Project  
**Timeline:** 2.5 months (10 weeks)  
**Team Size:** 7 (1 PM, 2 SA, 4 Dev)  
**Last Updated:** October 16, 2025

---

## 📋 Table of Contents

1. [Executive Summary](#executive-summary)
2. [Product Overview](#product-overview)
3. [Business Model](#business-model)
4. [User Roles](#user-roles)
5. [Feature Priorities](#feature-priorities)
6. [Critical Gaps Identified](#critical-gaps-identified)
7. [System Flows](#system-flows)
8. [Technical Requirements](#technical-requirements)
9. [Timeline & Milestones](#timeline--milestones)
10. [Team Responsibilities](#team-responsibilities)

---

## Executive Summary

**EventConnect** is an event management and ticketing platform that connects Event Organizers with participants, featuring automated payment processing and digital certificate generation.

### Core Value Propositions:
- **For Event Organizers:** End-to-end event management from promotion to participant certification
- **For Participants:** Discover events, purchase tickets, attend via QR code, receive automated certificates
- **For Platform:** Revenue through commission-based model (10% platform fee)

### Key Differentiators:
1. QR-based attendance system (paperless)
2. Automated certificate generation (feedback-gated)
3. Integrated payment and withdrawal system
4. All-in-one solution for event lifecycle

---

## Product Overview

### What is EventConnect?

A web-based platform enabling:
1. **Event Organizers** to create and manage paid/free events
2. **Participants** to browse, register, pay, attend, and receive certificates
3. **Admins** to oversee platform operations, user management, and financial transactions

### Target Users:
- Event Organizers (webinar hosts, workshop creators, seminar organizers)
- Event Participants (professionals, students, enthusiasts)
- Platform Administrators (internal team)

---

## Business Model

### Revenue Stream: Commission-Based

```
Participant Payment Flow:
─────────────────────────────────────
Participant pays: Rp 100,000
  ↓
Payment Gateway (Midtrans/Xendit): -2% = Rp 2,000
  ↓
Platform holds: Rp 98,000
  ↓
Platform Fee (10%): Rp 9,800
  ↓
EO receives: Rp 88,200 (available for withdrawal)
```

### Key Financial Rules:
- Platform fee: **10% of event price** (hardcoded for MVP)
- Minimum withdrawal: **Rp 50,000**
- Withdrawal processing: **Manual approval by Admin**
- Payment gateway: Midtrans or Xendit integration

---

## User Roles

### 1. Participant (Event Attendee)
**Can:**
- Register/login (email or Google SSO)
- Browse and search events
- Filter events by category, paid/free, date
- Join events (free or paid)
- Make payments for paid events
- Scan QR code for attendance
- Submit feedback after event
- Download certificate (after feedback submission)
- View "My Events" (upcoming & past)
- View payment history

**Cannot:**
- Create events
- Access other participants' data

---

### 2. Event Organizer (EO)
**Can:**
- All Participant capabilities, plus:
- Create/edit/delete events
- Upload event images and documentation
- Set event details (name, date, category, description, quota, price)
- Generate QR codes for events
- View participant list with attendance status
- Export participant list (CSV/Excel)
- View event statistics (attendance, revenue)
- View feedback from participants
- Request withdrawal
- View balance and transaction history
- Manage bank account information

**Cannot:**
- Approve withdrawals
- Delete other organizers' events
- Access platform-wide statistics

---

### 3. Admin
**Can:**
- View all users (EOs and Participants)
- Suspend/delete problematic users
- View all events across platform
- View platform statistics:
  - Total users (EOs, Participants, Premium Users)
  - Total events
  - Total revenue
- Approve/reject withdrawal requests
- Add/edit/delete event categories
- Monitor platform activity

**Cannot:**
- Edit users' personal information
- Directly transfer funds (manual bank transfer)

---

## Feature Priorities

### ✅ Must Have (Core MVP - Week 1-7)

#### Authentication & Profile Management
- User registration (Full Name, Email, Password)
- Login (Email/Password or Google SSO)
- Forgot Password flow
- View/Edit profile (Name, Email, Password)

#### Event Management (EO)
- **Create Event:** Input name, date, category, description, quota, price (free/paid)
- **Edit Event:** Modify event details (only before event starts)
- **Delete Event:** Remove event (only if no participants joined)
- **Event Dashboard:** View participant list with attendance status
- **Statistics:** View attendance count and revenue
- **Generate QR Code:** Unique QR per event for check-in
- **View Feedback:** See participant ratings and comments
- **Export Participants:** Download CSV/Excel of participant list

#### Event Discovery (Participant)
- **Homepage:** Display all available open events
- **Search Event:** Search by event name
- **Filter Event:** By category, paid/free, date, status (newest/oldest)
- **Event Details:** Full event information page
- **Join Event:** One-click registration (free) or payment page (paid)

#### Event Participation
- **My Events Page:** View upcoming and past events
- **Attendance:** Scan QR code to mark attendance (EO scans participant's QR)
- **Feedback Form:** Required feedback after event (rating 1-5 + comments)
- **Certificate Download:** Auto-generate PDF certificate after feedback submission

#### Payment System
- Payment gateway integration (Midtrans/Xendit)
- Payment status tracking (pending/success/failed)
- Payment confirmation page

#### **Financial System (CRITICAL - Week 7)** ⚠️
##### EO Side:
- **Balance Dashboard:**
  - Total Earned
  - Available Balance (after platform fee)
  - Already Withdrawn
- **Withdrawal Request:**
  - Input: Amount, Bank Name, Account Number, Account Name
  - Minimum withdrawal: Rp 50,000
  - Submit request → status: "Pending"
- **Withdrawal History:**
  - View all withdrawal requests
  - Status: Pending/Approved/Rejected/Transferred
  - Transaction dates

##### Admin Side:
- **Withdrawal Management:**
  - View all withdrawal requests
  - Approve/Reject with notes
  - Mark as "Transferred" after manual bank transfer
- **Platform Fee Settings:**
  - Set commission percentage (hardcode 10% for MVP)

##### System Logic:
```javascript
Available Balance = (Total Event Revenue) - (Platform Fee 10%) - (Already Withdrawn Amount)
```

#### Notifications (Automated)
- **Event Reminders:** 1 day and 1 hour before event
- **Attendance Reminder:** If user hasn't checked in yet
- **Payment Confirmation:** After successful payment
- **Summary Notification:** Post-event summary (participant count, feedback)

#### Dashboard
- **EO Dashboard:** Platform statistics (participant count per event, revenue)
- **Admin Dashboard:** Platform-wide stats (total users, events, revenue, premium users)

---

### 📦 Should Have (Nice to Have - Week 8-9)

#### Event Features
- **Bookmark Event:** Save events for later
- **Share Event:** Social sharing
- **Feedback Summarize:** AI-generated summary of all feedback
- **Template Certificate:** EO can upload logo/branding for auto-generated certificates
- **Participant Management:** Search participant by name/email

#### User Features
- **Payment History:** Detailed transaction log
- **Attendance History:** Track all attended events

#### Admin Features
- **Revenue Event Tracking:** Detailed revenue per event
- **Search Participant:** Platform-wide participant search
- **Sharing Material:** EO can upload slides/docs for participants

---

### 🎁 Could Have (Bonus Features - If Time Permits)

#### Advanced Features
- **Google SSO:** Register/login with Google account
- **In-App Notifications:** Real-time notifications within app
- **Face Recognition:** Alternative attendance tracking (AI-based)
- **Summary Event Notifications:** Automated event recap
- **Participant Join Notifications:** Notify EO when someone joins
- **Quota Full Alert:** Alert participants when event is full
- **Total Revenue in all events:** Admin view of all-time revenue
- **Premium Subscription:** Unlimited events for EO
- **Upload Documentation:** Post-event materials
- **Reschedule Event:** Change event date
- **Add/Edit/Delete Category:** Admin can manage categories

---

### 🚫 Won't Have (Future Phases)

Features explicitly excluded from MVP:
- Custom certificate templates (EO-designed)
- Custom registration forms
- Offline event support
- Recurring events (daily scheduling)
- Chat/Groups feature
- Refund management (handle manually)
- Event recurring automation

---

## Critical Gaps Identified

### ❌ Previously Missing Features (Now Added):

1. **Withdrawal System** ⚠️ **MOST CRITICAL**
   - **Problem:** Platform collects payment but no way for EO to withdraw earnings
   - **Solution:** Added complete withdrawal flow (request → approval → transfer)
   - **Impact:** Without this, business model doesn't work

2. **Platform Fee Logic**
   - **Problem:** No clear definition of how platform makes money
   - **Solution:** Defined 10% commission on all paid events
   - **Impact:** Revenue model now transparent

3. **Balance Tracking**
   - **Problem:** EO can't see their earnings
   - **Solution:** Dashboard showing total earned, available balance, withdrawn
   - **Impact:** Financial transparency for EO

4. **Financial Admin Panel**
   - **Problem:** No way for admin to manage payouts
   - **Solution:** Approval system for withdrawal requests
   - **Impact:** Manual control over cash flow

### ✅ Edge Cases Covered:

- Event with zero participants → can delete
- Event with participants → cannot delete
- Feedback required before certificate download
- Minimum withdrawal amount to reduce processing
- Payment failure handling

---

## System Flows

### 1. Event Creation Flow (EO)
```
EO Login → Dashboard → Create Event → Fill Form (name, date, category, desc, quota, price) 
→ Upload Image → Submit → Event Published → Generate QR Code
```

### 2. Event Participation Flow (Participant)
```
Browse Events → Search/Filter → Event Details → Join Event
  ↓
If Free: Confirm → Success
If Paid: Payment Gateway → Success → Payment Confirmation
  ↓
Event Day → Scan QR Code → Attendance Marked
  ↓
After Event → Submit Feedback (rating + comments) → Certificate Generated → Download PDF
```

### 3. Withdrawal Flow (EO)
```
EO Dashboard → View Balance → Request Withdrawal → Input Amount + Bank Details 
→ Submit → Status: Pending
  ↓
Admin Reviews → Approve/Reject
  ↓
If Approved → Manual Bank Transfer → Admin Marks as "Transferred" → EO Receives Funds
```

### 4. Payment Flow
```
Participant Pays Rp 100,000
  ↓
Payment Gateway (Midtrans) → Deduct 2% = Rp 2,000
  ↓
Platform Receives Rp 98,000
  ↓
Platform Fee 10% = Rp 9,800
  ↓
EO Available Balance: Rp 88,200
  ↓
EO Requests Withdrawal → Admin Approves → Manual Transfer to EO Bank
```

---

## Technical Requirements

### Tech Stack (Suggested)
- **Frontend:** React.js / Next.js
- **Backend:** Node.js + Express / Laravel
- **Database:** PostgreSQL / MySQL
- **Payment Gateway:** Midtrans or Xendit
- **QR Code:** QRCode.js library
- **PDF Generation:** jsPDF or PDFKit
- **Authentication:** JWT + Google OAuth
- **Hosting:** Vercel (FE) + Railway/Heroku (BE)

### Database Schema (Key Tables)

#### Users
```sql
- id
- name
- email
- password (hashed)
- role (participant/event_organizer/admin)
- is_verified
- created_at
```

#### Events
```sql
- id
- organizer_id (FK to users)
- name
- description
- category_id (FK to categories)
- date
- quota
- price (0 for free events)
- status (upcoming/ongoing/ended)
- qr_code
- image_url
- created_at
```

#### Participants (Event Registrations)
```sql
- id
- event_id (FK to events)
- user_id (FK to users)
- payment_status (free/pending/paid)
- attendance_status (absent/present)
- feedback_submitted (boolean)
- certificate_url
- joined_at
```

#### Withdrawals ⚠️ **NEW TABLE**
```sql
- id
- organizer_id (FK to users)
- amount
- bank_name
- account_number
- account_name
- status (pending/approved/rejected/transferred)
- admin_notes
- requested_at
- processed_at
- processed_by (FK to users - admin)
```

#### Transactions
```sql
- id
- event_id (FK to events)
- user_id (FK to users - participant)
- amount
- platform_fee
- organizer_earning
- payment_gateway_reference
- status (pending/success/failed)
- created_at
```

#### Feedback
```sql
- id
- event_id (FK to events)
- user_id (FK to users)
- rating (1-5)
- comment
- created_at
```

### API Endpoints (Key Routes)

#### Authentication
- `POST /api/auth/register`
- `POST /api/auth/login`
- `POST /api/auth/google`
- `POST /api/auth/forgot-password`
- `POST /api/auth/reset-password`

#### Events (Public)
- `GET /api/events` (search, filter)
- `GET /api/events/:id`

#### Events (EO)
- `POST /api/events` (create)
- `PUT /api/events/:id` (edit)
- `DELETE /api/events/:id`
- `GET /api/events/:id/participants`
- `GET /api/events/:id/feedback`
- `POST /api/events/:id/qr-generate`

#### Participation
- `POST /api/events/:id/join`
- `POST /api/events/:id/attendance`
- `POST /api/events/:id/feedback`
- `GET /api/events/:id/certificate`

#### Financial ⚠️ **CRITICAL ENDPOINTS**
- `GET /api/organizer/balance` (view balance)
- `POST /api/organizer/withdrawal/request`
- `GET /api/organizer/withdrawal/history`
- `GET /api/admin/withdrawals` (admin view all)
- `PATCH /api/admin/withdrawals/:id/approve`
- `PATCH /api/admin/withdrawals/:id/reject`

#### Payments
- `POST /api/payments/create`
- `POST /api/payments/callback` (webhook from gateway)
- `GET /api/payments/history`

---

## Timeline & Milestones

### Week 1-2: Setup & Foundation
- [x] Project kickoff meeting
- [x] Requirement analysis
- [x] Tech stack decision
- [ ] Database design
- [ ] Project repository setup
- [ ] Authentication system

**Deliverable:** Working login/register

---

### Week 3-4: Core Event Features
- [ ] Event CRUD (Create, Read, Update, Delete)
- [ ] Event search and filter
- [ ] Event details page
- [ ] Category management
- [ ] Image upload

**Deliverable:** EO can create and manage events

---

### Week 5-6: Participation & Payment
- [ ] Join event functionality
- [ ] Payment gateway integration
- [ ] QR code generation
- [ ] Attendance scanning
- [ ] Payment confirmation page

**Deliverable:** Participants can join and pay for events

---

### Week 7: Financial System ⚠️ **CRITICAL WEEK**
- [ ] Balance dashboard (EO)
- [ ] Withdrawal request form
- [ ] Withdrawal history page
- [ ] Admin withdrawal approval panel
- [ ] Platform fee calculation logic
- [ ] Transaction logging

**Deliverable:** Complete withdrawal system working end-to-end

---

### Week 8: Feedback & Certificates
- [ ] Feedback form
- [ ] Certificate PDF generation
- [ ] Download certificate
- [ ] Feedback summary for EO
- [ ] Rating system

**Deliverable:** Participants can submit feedback and download certificates

---

### Week 9: Notifications & Dashboard
- [ ] Email notification system
- [ ] Event reminders (1 day, 1 hour before)
- [ ] Payment confirmations
- [ ] EO dashboard with statistics
- [ ] Admin dashboard

**Deliverable:** Automated notification system and analytics

---

### Week 10: Polish & Testing
- [ ] Bug fixing
- [ ] UI/UX improvements
- [ ] User acceptance testing
- [ ] Documentation
- [ ] Deployment
- [ ] Final presentation preparation

**Deliverable:** Production-ready application + documentation

---

## Team Responsibilities

### PM (You)
**Primary Responsibilities:**
- Define product vision and roadmap
- Prioritize features (Must/Should/Could/Won't Have)
- Facilitate team meetings (daily standup, weekly review)
- Quality assurance on deliverables
- Remove blockers
- Stakeholder communication
- Documentation oversight

**DON'T:**
- Write code (unless emergency)
- Create detailed specs yourself (delegate to SA)
- Micromanage developers

**Key Activities:**
- Daily: Check progress, unblock issues
- Weekly: Review meeting, demo, planning
- Bi-weekly: Stakeholder update

---

### System Analysts (2)
**Primary Responsibilities:**
- Analyze requirements and business logic
- Create functional specifications
- Design system flows and diagrams
- Identify edge cases and gaps
- Document API requirements
- Present specs to developers

**Assignment:**
- **SA 1:** Authentication, Profile, Event Management
- **SA 2:** Payment, Withdrawal, Certificate, Notifications

**Checklist per Feature:**
```
☐ Happy path flow documented
☐ Error/edge cases identified
☐ Data flow mapped (input → process → output)
☐ Related features analyzed
☐ Security/validation requirements defined
☐ Financial implications considered (if applicable)
☐ API endpoints specified
☐ Database schema defined
```

---

### Frontend Developers (2)
**Primary Responsibilities:**
- Implement UI/UX based on designs
- API integration
- State management
- Form validation
- Responsive design

**Assignment:**
- **FE Dev 1:** Auth pages, Event pages, Homepage
- **FE Dev 2:** Payment flow, Dashboard, Certificate download

---

### Backend Developers (2)
**Primary Responsibilities:**
- Build RESTful APIs
- Database design and implementation
- Business logic implementation
- Payment gateway integration
- Authentication and authorization

**Assignment:**
- **BE Dev 1:** Auth API, Event API, Search/Filter
- **BE Dev 2:** Payment API, Withdrawal API, Notification system

---

## Communication & Collaboration

### Daily Standup (15 min - WhatsApp/Online)
**Format:**
- What did I do yesterday?
- What will I do today?
- Any blockers?

### Weekly Review (1 hour - Google Meet)
**Agenda:**
1. Demo completed features (10 min)
2. Review SA specs for next sprint (15 min)
3. Discuss blockers and solutions (15 min)
4. Plan next week's tasks (15 min)
5. Q&A (5 min)

### Tools
- **Task Management:** Trello / Notion
- **Communication:** WhatsApp Group
- **Code Repository:** GitHub
- **Design:** Figma
- **Documentation:** Google Docs / Notion

---

## Quality Standards

### Code Review Requirements
- All code must be reviewed by at least 1 other developer
- No direct commits to `main` branch
- Use feature branches: `feature/event-creation`

### Testing Requirements
- Manual testing before marking task as "Done"
- Test on multiple browsers (Chrome, Firefox, Safari)
- Mobile responsiveness check

### Documentation Requirements
- API endpoints documented with examples
- Complex business logic commented in code
- README with setup instructions

---

## Risk Management

### High-Risk Items
1. **Payment Gateway Integration** (Week 5-6)
   - **Risk:** Complex API, potential delays
   - **Mitigation:** Start early, use sandbox mode, read docs thoroughly

2. **Withdrawal System** (Week 7)
   - **Risk:** Critical for business model, complex logic
   - **Mitigation:** Prioritize this week, allocate best developers, thorough testing

3. **QR Code Scanning** (Week 6)
   - **Risk:** May not work on all devices
   - **Mitigation:** Use proven library (QRCode.js), test on multiple devices

### Medium-Risk Items
- Certificate PDF generation (use established libraries)
- Email notifications (use SendGrid/Mailgun)
- Google SSO integration (follow official docs)

---

## Success Metrics

### Technical Metrics
- [ ] 100% Must Have features completed
- [ ] <5 critical bugs at launch
- [ ] All API endpoints tested and documented
- [ ] Mobile responsive on 3+ screen sizes

### Functional Metrics
- [ ] User can register → login → browse → join event → pay → attend → feedback → certificate (full flow)
- [ ] EO can create event → view participants → approve attendance → view feedback → withdraw funds
- [ ] Admin can view stats → approve withdrawals → manage users

### Academic Metrics
- [ ] Complete project documentation
- [ ] Working demo for presentation
- [ ] Code repository with clean commit history
- [ ] User manual / guide

---

## Notes & Decisions Log

### Key Decisions Made
1. **Platform Fee:** 10% commission (hardcoded for MVP)
2. **Minimum Withdrawal:** Rp 50,000
3. **Payment Gateway:** Midtrans (primary choice)
4. **Certificate Requirement:** Must submit feedback first
5. **Withdrawal Processing:** Manual approval by admin (no auto-transfer)
6. **Google SSO:** Should Have (not Must Have)
7. **Event Approval:** No admin approval needed (auto-publish)

### Features Explicitly Cut
- Custom certificate templates → Use single default template
- Refund system → Handle manually via support
- Chat/messaging → Not needed for MVP
- Event recurring → Manual creation only
- Offline events → Online-only for MVP

---

## Appendix

### Glossary
- **EO:** Event Organizer
- **MVP:** Minimum Viable Product
- **QR:** Quick Response (code)
- **SSO:** Single Sign-On
- **CRUD:** Create, Read, Update, Delete
- **API:** Application Programming Interface

### Reference Links
- Payment Gateway: [Midtrans Docs](https://docs.midtrans.com)
- QR Code Library: [QRCode.js](https://davidshimjs.github.io/qrcodejs/)
- PDF Generation: [jsPDF](https://github.com/parallax/jsPDF)

---

## Change Log

| Date | Version | Changes | Author |
|------|---------|---------|--------|
| 2025-10-16 | 1.0 | Initial documentation created | PM |
| TBD | 1.1 | Added withdrawal system details | PM |

---

**Document Status:** ✅ Approved for Development

**Next Review Date:** Week 5 (Mid-project checkpoint)

---

*For questions or clarifications, contact PM via project WhatsApp group.*
