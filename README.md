# FastAPI Study Tracker

A comprehensive study tracking application built with FastAPI, designed to help students and learners track their study sessions, manage subjects, and monitor progress toward learning goals.

## Features

- **User Management**: Create accounts and manage user profiles
- **Subject Tracking**: Organize study materials by subjects with custom colors
- **Study Sessions**: Log study sessions with duration, notes, and descriptions
- **Goal Setting**: Set learning goals with target hours and deadlines
- **Progress Tracking**: Monitor completion progress and study statistics
- **RESTful API**: Complete REST API for all operations

## Technology Stack

- **Backend**: FastAPI
- **Database**: SQLAlchemy ORM with PostgreSQL/SQLite support
- **Validation**: Pydantic
- **Server**: Uvicorn
- **Testing**: Pytest

## Installation

### Prerequisites
- Python 3.9+
- PostgreSQL (optional, SQLite is default)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/nursultanbeishenbekov20008-cmyk/fastapi-study-tracker.git
cd fastapi-study-tracker
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Initialize the database:
```bash
python -m alembic upgrade head
```

6. Run the application:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the application is running, you can access:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Project Structure

```
fastapi-study-tracker/
├── main.py              # Application entry point
├── config.py            # Configuration settings
├── database.py          # Database setup and session management
├── models.py            # SQLAlchemy models
├── schemas.py           # Pydantic schemas for validation
├── requirements.txt     # Python dependencies
├── .env.example         # Example environment variables
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## API Endpoints

### Users
- `POST /api/v1/users/register` - Create a new user
- `GET /api/v1/users/me` - Get current user profile
- `PUT /api/v1/users/me` - Update user profile

### Subjects
- `GET /api/v1/subjects` - List all subjects
- `POST /api/v1/subjects` - Create a new subject
- `GET /api/v1/subjects/{id}` - Get subject details
- `PUT /api/v1/subjects/{id}` - Update a subject
- `DELETE /api/v1/subjects/{id}` - Delete a subject

### Study Sessions
- `GET /api/v1/sessions` - List study sessions
- `POST /api/v1/sessions` - Create a new study session
- `GET /api/v1/sessions/{id}` - Get session details
- `PUT /api/v1/sessions/{id}` - Update a session
- `DELETE /api/v1/sessions/{id}` - Delete a session

### Goals
- `GET /api/v1/goals` - List all goals
- `POST /api/v1/goals` - Create a new goal
- `GET /api/v1/goals/{id}` - Get goal details
- `PUT /api/v1/goals/{id}` - Update a goal
- `DELETE /api/v1/goals/{id}` - Delete a goal

## Testing

Run tests with:
```bash
pytest
```

Run tests with coverage:
```bash
pytest --cov=.
```

## Environment Variables

See `.env.example` for all available configuration options:

- `DATABASE_URL`: Database connection string
- `DEBUG`: Enable debug mode
- `ENVIRONMENT`: Application environment (development/production)
- `SECRET_KEY`: Secret key for authentication
- `CORS_ORIGINS`: Allowed CORS origins

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, open an issue on the GitHub repository.

## Roadmap

- [ ] Authentication and JWT tokens
- [ ] User dashboard with statistics
- [ ] Study streak tracking
- [ ] Export study data
- [ ] Mobile app
- [ ] Integration with calendar services
- [ ] Advanced analytics