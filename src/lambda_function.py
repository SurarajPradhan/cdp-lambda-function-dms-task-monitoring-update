from datetime import datetime
import json
import boto3

# Initialize DynamoDB resource
ddb = boto3.resource('dynamodb')
table = ddb.Table('cdp_dev_dic_dms_task_tracker')


def lambda_handler(event, context):
    try:
        print(f'event : {event}')
        print(f'context : {context}')

        # Extract event parameters
        # cdi_sf_execution_id = event['cdi_sf_execution_id']
        # cdi_dms_task_name = event['cdi_dms_task_name']
        # cdi_dms_task_stats_FullLoadFinishDate = event.get('cdi_dms_task_stats_FullLoadFinishDate')
        # cdi_dms_task_stats_ElapsedTimeMillis = event.get('cdi_dms_task_stats_ElapsedTimeMillis')
        # cdi_dms_task_stats_FullLoadProgressPercent = event.get('cdi_dms_task_stats_FullLoadProgressPercent')
        # cdi_dms_task_State = event.get('cdi_dms_task_State')
        #
        ## Get the current timestamp
        # update_timestamp = str(datetime.now())

        ## Define the update expression conditionally
        # update_expression = 'SET update_timestamp = :upd_ts'
        #
        ## Add optional attributes to the update expression if they exist
        # if cdi_dms_task_stats_FullLoadFinishDate is not None:
        #    update_expression += ', FullLoadFinishDate = :v_FullLoadFinishDate'
        #
        # if cdi_dms_task_stats_ElapsedTimeMillis is not None:
        #    update_expression += ', ElapsedTimeMillis = :v_ElapsedTimeMillis'
        #
        # if cdi_dms_task_stats_FullLoadProgressPercent is not None:
        #    update_expression += ', FullLoadProgressPercent = :v_FullLoadProgressPercent'

        # if cdi_dms_task_State is not None:
        #    update_expression += ', job_state = :v_cdi_dms_task_State'

        # Update the DynamoDB item
        # table.update_item(
        #    Key={
        #        'dms_task_name': cdi_dms_task_name,
        #        'sf_execution_id': cdi_sf_execution_id
        #    },
        #    UpdateExpression=update_expression,
        #    ExpressionAttributeValues={
        #        ':upd_ts': update_timestamp,
        #        ':v_cdi_dms_task_State': cdi_dms_task_State,
        #        ':v_FullLoadFinishDate': cdi_dms_task_stats_FullLoadFinishDate,
        #        ':v_ElapsedTimeMillis': cdi_dms_task_stats_ElapsedTimeMillis,
        #        ':v_FullLoadProgressPercent': cdi_dms_task_stats_FullLoadProgressPercent
        #    }
        # )

        return {
            'statusCode': 200,
            'body': json.dumps('Data_Ingestion_Tracker_Metadata is updated.')
        }
    except Exception as e:
        # Handle and log any exceptions
        error_message = f"Error: {str(e)}"
        print(error_message)
        return {
            'statusCode': 500,
            'body': json.dumps(error_message)
        }
