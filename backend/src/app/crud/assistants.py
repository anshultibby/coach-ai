from app.core.supabase import supabase
from app.models.assistants import Assistant, AssistantResponse

def create_assistant(assistant: Assistant) -> AssistantResponse:
    data = {
        "name": assistant.name,
        "config": {"prompt": assistant.prompt}
    }
    response = supabase.table('assistants').insert(data).execute()
    data = response.data[0]
    return AssistantResponse(
        id=data["id"],
        name=data["name"],
        prompt=data["config"]["prompt"]
    )

def get_assistant(assistant_id: str) -> AssistantResponse:
    response = supabase.table('assistants').select("*").eq('id', assistant_id).execute()
    if not response.data:
        return None
    data = response.data[0]
    return AssistantResponse(
        id=data["id"],
        name=data["name"],
        prompt=data["config"]["prompt"]
    )

def list_assistants() -> list[AssistantResponse]:
    response = supabase.table('assistants').select("*").execute()
    return [
        AssistantResponse(
            id=item["id"],
            name=item["name"],
            prompt=item["config"]["prompt"]
        )
        for item in response.data
    ]

def update_assistant(assistant_id: str, assistant: Assistant) -> AssistantResponse:
    data = {
        "name": assistant.name,
        "config": {"prompt": assistant.prompt}
    }
    response = supabase.table('assistants').update(data).eq('id', assistant_id).execute()
    if not response.data:
        return None
    data = response.data[0]
    return AssistantResponse(
        id=data["id"],
        name=data["name"],
        prompt=data["config"]["prompt"]
    ) 