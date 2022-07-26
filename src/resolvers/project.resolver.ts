import { Resolver, Query, Args, ID } from '@nestjs/graphql';
import { Field, Int, ObjectType } from '@nestjs/graphql';
import { DynamoDB } from "aws-sdk";
import { GetItemOutput } from 'aws-sdk/clients/dynamodb';
import { DocumentClient } from 'src/config/dynamodb.config';


@ObjectType()
class Project {
  @Field(() => ID)
  ID!: string;

  @Field()
  data!: string;
}


@Resolver()
class ProjectsResolver {

  @Query(() => Project)
  async getProjects(@Args('id', { type: () => String }) id: string) {
    const result = await DocumentClient
      .get({
        TableName: "projects_cache",
        Key: {
          ID: id,
        },
      })
      .promise()
      .then(data => data.Item);

    console.log(result);
    return result;
  }

}

export { ProjectsResolver };