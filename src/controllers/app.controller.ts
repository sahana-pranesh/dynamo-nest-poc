import { Body, Controller, Get, Post } from '@nestjs/common';
import { ChartRequest } from 'src/dto/chart.request';
import { AppService } from '../services/app.service';

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get('/hello')
  getHello(): string {
    return this.appService.getHello();
  }

  @Post('/chart')
  insertChart(@Body() request: ChartRequest) {
    console.log('Incoming request' , request);
    return this.appService.insertChart(request);
  }
}
