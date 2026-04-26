import uuid
from fastapi import APIRouter, HTTPException, status
from app.schemas import IssueCreate, IssueOut, IssueStatus, IssueUpdate
from app.storage import load_data, save_data

router = APIRouter(prefix="/api/v1/issues", tags=["issues"])

@router.get("/", response_model=list[IssueOut])
def get_issues():
    ''' retrive all issues'''
    # the response it  list using a issueout schema
    issues = load_data()
    return issues

@router.post("/", response_model=IssueOut, status_code = status.HTTP_201_CREATED)
def create_issue(payload: IssueCreate):
    '''create a new issue'''
    # the issue out is not a list because we are creating one issue
    issues = load_data()
    new_issue = {
        "id" : str(uuid.uuid4()),
        "title" : payload.title,
        "description": payload.description,
        "priority" : payload.priority,
        "status": IssueStatus.open
    }
    issues.append(new_issue)
    save_data(issues)
    return new_issue

# get a specific issue by id
@router.get("/{issue_id}", response_model=IssueOut)
def get_issue(issue_id: str):
    '''retrive a specific issue by id'''
    issues = load_data()
    for issue in issues:
        if issue["id"] == issue_id:
            return issue
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")

# update an issue
@router.put("/{issue_id}", response_model=IssueOut)
def update_issue(issue_id: str, payload: IssueUpdate):
    '''update an issue'''
    issues = load_data()
    for issue in issues:
        if issue["id"] == issue_id:
            if payload.title is not None:
                issue["title"] = payload.title
            if payload.description is not None:
                issue["description"] = payload.description
            if payload.priority is not None:
                issue["priority"] = payload.priority
            if payload.status is not None:
                issue["status"] = payload.status
            save_data(issues)
            return issue
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")


#  delete an issue
@router.delete("/{issue_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_issue(issue_id:str):
    '''delete an issue by id'''
    issues = load_data()
    for i, issue in enumerate(issues):
        if issue["id"] == issue_id:
            issues.pop(i)
            save_data(issues)
            return 
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")


        