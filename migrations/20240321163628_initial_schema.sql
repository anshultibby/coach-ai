-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Create role enum type
CREATE TYPE message_role AS ENUM ('user', 'assistant', 'system');

-- Users table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    dob DATE NOT NULL,
    phone_number TEXT NOT NULL UNIQUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT phone_number_format CHECK (phone_number ~ '^\+?[1-9]\d{1,14}$')
);

-- Assistants table
CREATE TABLE assistants (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name TEXT NOT NULL,
    config JSONB NOT NULL DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Sessions table
CREATE TABLE sessions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id),
    assistant_id UUID NOT NULL REFERENCES assistants(id),
    start_time TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Messages table
CREATE TABLE messages (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    session_id UUID NOT NULL REFERENCES sessions(id),
    role message_role NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes
CREATE INDEX idx_sessions_user_id ON sessions(user_id);
CREATE INDEX idx_messages_session_id ON messages(session_id);
CREATE INDEX idx_users_phone_number ON users(phone_number);

-- Add comments
COMMENT ON TABLE users IS 'Store user information for the AI health coach system';
COMMENT ON TABLE sessions IS 'Track conversation sessions between users and AI assistants';
COMMENT ON TABLE messages IS 'Store individual messages within a conversation session';
COMMENT ON TABLE assistants IS 'Configure different AI assistant personalities and behaviors'; 